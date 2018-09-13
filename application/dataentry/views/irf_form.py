import json
import pytz
import traceback

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import filters as fs
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import default_storage
from django.db import IntegrityError
from dataentry.serialize_form import FormDataSerializer
from dataentry.serializers import CountrySerializer
from dataentry.dataentry_signals import form_done

from dataentry.form_data import Form, FormData
from dataentry.models import BorderStation, Country, FormType, IrfNepal, UserLocationPermission

class BorderStationOverviewSerializer(serializers.ModelSerializer):
    operating_country = CountrySerializer()
    class Meta:
        fields = [
            'id',
            'station_code',
            'station_name',
            'operating_country',
        ]
        model = BorderStation

class IrfListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    irf_number = serializers.CharField()
    number_of_victims = serializers.IntegerField()
    number_of_traffickers = serializers.IntegerField()
    staff_name = serializers.CharField()
    date_time_of_interception = serializers.SerializerMethodField(read_only=True)
    date_time_entered_into_system = serializers.SerializerMethodField(read_only=True)
    date_time_last_updated = serializers.SerializerMethodField(read_only=True)
    station = BorderStationOverviewSerializer()
    form_name = serializers.SerializerMethodField(read_only=True)
    can_view = serializers.SerializerMethodField(read_only=True)
    can_edit = serializers.SerializerMethodField(read_only=True)
    can_delete = serializers.SerializerMethodField(read_only=True)
    can_approve = serializers.SerializerMethodField(read_only=True)
    
    perm_group_name = 'IRF'
    
    def adjust_date_time_for_tz(self, date_time, tz_name):
        tz = pytz.timezone(tz_name)
        date_time = date_time.astimezone(tz)
        date_time = date_time.replace(microsecond=0)
        date_time = date_time.replace(tzinfo=None)
        return str(date_time)
    
    def get_date_time_of_interception(self, obj):
        return self.adjust_date_time_for_tz (obj.date_time_of_interception, obj.station.time_zone)
    
    def get_date_time_entered_into_system(self, obj):
        return self.adjust_date_time_for_tz (obj.date_time_entered_into_system, obj.station.time_zone)
    
    def get_date_time_last_updated(self, obj):
        return self.adjust_date_time_for_tz (obj.date_time_last_updated, obj.station.time_zone)
    
    def get_form_name(self, obj):
        forms = Form.objects.filter(form_type__name='IRF', stations__id=obj.station.id)
        if len(forms) > 0:
            return forms[0].form_name
        else:
            return None
    
    def get_can_view(self, obj):
        perm_list = self.context.get('perm_list')
        return UserLocationPermission.has_permission_in_list(perm_list, self.perm_group_name,'VIEW', obj.station.operating_country.id, obj.station.id)
    
    def get_can_edit(self, obj):
        perm_list = self.context.get('perm_list')
        ret =  UserLocationPermission.has_permission_in_list(perm_list, self.perm_group_name,'EDIT', obj.station.operating_country.id, obj.station.id)
        return ret
    
    def get_can_delete(self, obj):
        perm_list = self.context.get('perm_list')
        return UserLocationPermission.has_permission_in_list(perm_list, self.perm_group_name,'DELETE', obj.station.operating_country.id, obj.station.id)
    
    def get_can_approve(self, obj):
        perm_list = self.context.get('perm_list')
        return UserLocationPermission.has_permission_in_list(perm_list, self.perm_group_name,'APPROVE', obj.station.operating_country.id, obj.station.id)

class IrfFormViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    permission_classes = (IsAuthenticated, )
    serializer_class = IrfListSerializer
    filter_backends = (fs.SearchFilter, fs.OrderingFilter,)
    search_fields = ('irf_number',)
    ordering_fields = (
        'irf_number', 'staff_name', 'number_of_victims', 'number_of_traffickers', 'date_time_of_interception',
        'date_time_entered_into_system', 'date_time_last_updated',)
    ordering = ('-date_time_of_interception',)
    form_type_name = 'IRF'
    perm_group_name = 'IRF'
    
    def get_serializer_class(self):
        if self.action == 'list':
            return IrfListSerializer
        else:
            return FormDataSerializer
    
    def get_serializer_context(self): 
        return self.serializer_context
    
    def get_queryset(self):
        if self.action != 'list':
            return None
        in_country = self.request.GET.get('country_ids')
        status = self.request.GET.get('status', 'approved')
        search = self.request.GET.get('search')
                
        countries = Country.objects.all()
        all_country_list = []
        for country in countries:
            all_country_list.append(country.id)
        
        country_list = []
        if in_country is not None and in_country != '':
            # client provided a list of countries to consider
            for cntry in in_country.split(','):
                country_list.append(int(cntry))
        else:
            # client did not provide a list - so consider all countries
           country_list = all_country_list
        
        account_id = self.request.user.id
        
        station_list = []
        form_list = []
        tmp_station_list = BorderStation.objects.filter(operating_country__in=country_list)
        perm_list = UserLocationPermission.objects.filter(account__id=account_id, permission__permission_group=self.perm_group_name).exclude(permission__action='ADD')
        self.serializer_context = {'perm_list':perm_list}
        for station in tmp_station_list:
            if (UserLocationPermission.has_permission_in_list(perm_list, self.perm_group_name, None, station.operating_country.id, station.id)):
                station_list.append(station)
                form = Form.current_form(self.form_type_name, station.id)
                if form is not None and form not in form_list:
                    form_list.append(form)
        
        queryset = None
        for form in form_list:
            mod = __import__(form.storage.module_name, fromlist=[form.storage.form_model_name])
            form_model = getattr(mod, form.storage.form_model_name)
            
            tmp_queryset = form_model.objects.filter(station__in=station_list, status=status).only(
                    'id', 'irf_number', 'form_entered_by', 'number_of_victims', 'number_of_traffickers', 'staff_name', 
                    'station', 'date_time_of_interception', 'date_time_entered_into_system',
                    'date_time_last_updated')
            
            # If query is for in-progress status IRFs, only include IRFs that were entered by the requesters account
            if status == 'in-progress':
                tmp_queryset = tmp_queryset.filter(form_entered_by__id=account_id)
                
            if search is not None:
                tmp_queryset = tmp_queryset.filter(irf_number__contains=search)
            
            if queryset is None:
                queryset = tmp_queryset
            else:
                queryset = queryset.union(tmp_queryset)
            
        if queryset is None:
            queryset = IrfNepal.objects.none()
                
        return queryset
    
    def save_files(self, files, subdirectory):
        for file_obj in files:
            filename = file_obj.name
            with default_storage.open(subdirectory + filename, 'wb+') as destination:
                for chunk in file_obj.chunks():
                    destination.write(chunk)
    
    def extract_data(self, request):
        if 'main' in request.data:
            request_string = request.data['main']
            request_json = json.loads(request_string)
        
            cnt = 0
            images = []
            while 'images[' + str(cnt) + ']' in request.data:
                images.append(request.data['images[' + str(cnt) + ']'])
                cnt += 1
            
            self.save_files(images, 'interceptee_photos/')
            
            cnt = 0
            scanned = []
            while 'scanned[' + str(cnt) + ']' in request.data:
                scanned.append(request.data['scanned[' + str(cnt) + ']'])
                cnt += 1
            
            self.save_files(scanned, 'scanned_irf_forms/')
        else:
            request_json = None
        
        return request_json
    
    def create(self, request):
        form_type = FormType.objects.get(name=self.form_type_name)
        request_json = self.extract_data(request)
        self.serializer_context = {'form_type':form_type, 'request.user':request.user}
        try:
            serializer = FormDataSerializer(data=request_json, context=self.serializer_context)
            if serializer.is_valid():
                if not UserLocationPermission.has_session_permission(request, 'IRF', 'ADD', serializer.get_country_id(), serializer.get_station_id()):
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
                try:
                    form_data = serializer.save()
                    serializer2 = FormDataSerializer(form_data, context=self.serializer_context)
                    form_done.send_robust(sender=self.__class__, form_data=form_data)
                    ret = serializer2.data
                    rtn_status = status.HTTP_200_OK
                except IntegrityError as exc:
                    if 'unique constraint' in exc.args[0]:
                        ret = {
                            'errors': [ exc.args[0] ],
                            'warnings':[]
                        }
                        rtn_status=status.HTTP_400_BAD_REQUEST
                    else:
                        ret = {
                            'errors': [exc.args[0]],
                            'warnings':[]
                        }
                        rtn_status=status.HTTP_400_BAD_REQUEST
            else:
                ret = {
                    'errors': serializer.the_errors,
                    'warnings':serializer.the_warnings
                    }
                rtn_status=status.HTTP_400_BAD_REQUEST
        except Exception:
            if serializer.the_errors is not None and len(serializer.the_errors) > 0:
                rtn_errors = serializer.the_errors
            else:
                rtn_errors = []
                
            if serializer.the_warnings is not None and len(serializer.the_warnings) > 0:
                rtn_warnings = serializer.the_warnings
            else:
                rtn_warnings = []
            
            if len(rtn_errors) < 1 and len(rtn_warnings) < 1:
                rtn_errors = serializer._errors
            ret = {
                'errors': rtn_errors,
                'warnings':rtn_warnings
                }
            rtn_status = status.HTTP_500_INTERNAL_SERVER_ERROR
            
        return Response (ret, status=rtn_status)
        
    def retrieve_blank_form(self, request, station_id):
        self.serializer_context = {}
        form = Form.current_form(self.form_type_name, station_id)
        if form is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        form_class = FormData.get_form_class(form)
        irf = form_class()
        station = BorderStation.objects.get(id=station_id)
        irf.station = station
        add_access = UserLocationPermission.has_session_permission(request, 'IRF', 'ADD', irf.station.operating_country.id, irf.station.id)
        if not add_access:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        form_data = FormData(irf, form)
        serializer = FormDataSerializer(form_data, context=self.serializer_context)
        return Response(serializer.data)
    
    def my_retrieve(self, request, station_id, pk):
        self.serializer_context = {}
        form = Form.current_form(self.form_type_name, station_id)
        if form is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            irf = FormData.find_object_by_id(pk, form)
            if irf is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        read_access = UserLocationPermission.has_session_permission(request, 'IRF', 'VIEW', irf.station.operating_country.id, irf.station.id)
        edit_access = UserLocationPermission.has_session_permission(request, 'IRF', 'EDIT', irf.station.operating_country.id, irf.station.id)
        private_access = UserLocationPermission.has_session_permission(request, 'IRF', 'VIEW PI', irf.station.operating_country.id, irf.station.id)
        
        if not read_access:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
                
        if not edit_access and not private_access:
            self.serializer_context['mask_private'] = True
            
        form_data = FormData(irf, form)
        serializer = FormDataSerializer(form_data, context=self.serializer_context)
        
        resp_data = serializer.data
       
        return Response(resp_data)
    
    def update(self, request, station_id, pk):
        form = Form.current_form(self.form_type_name, station_id)
        irf = FormData.find_object_by_id(pk, form)
        if irf is None:
            return Response({'errors' : ["IRF not found"], 'warnings':[]}, status=status.HTTP_404_NOT_FOUND)
        form_data = FormData(irf, form)
        request_json = self.extract_data(request)

        self.serializer_context = {'form_type':form.form_type}
        try:
            serializer = FormDataSerializer(form_data, data=request_json, context=self.serializer_context)
        
            if serializer.is_valid():
                if not UserLocationPermission.has_session_permission(request, 'IRF', 'EDIT', serializer.get_country_id(), serializer.get_station_id()):
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
                form_data = serializer.save()
                serializer2 = FormDataSerializer(form_data, context=self.serializer_context)
                form_done.send_robust(sender=self.__class__, form_data=form_data)
                rtn_status = status.HTTP_200_OK
                ret = serializer2.data
            else:
                if serializer.the_errors is not None and len(serializer.the_errors) > 0:
                    rtn_errors = serializer.the_errors
                else:
                    rtn_errors = []
                    
                if serializer.the_warnings is not None and len(serializer.the_warnings) > 0:
                    rtn_warnings = serializer.the_warnings
                else:
                    rtn_warnings = []
                
                if len(rtn_errors) < 1 and len(rtn_warnings) < 1:
                    rtn_errors = serializer._errors
                ret = {
                    'errors': rtn_errors,
                    'warnings':rtn_warnings
                    }
                rtn_status = status.HTTP_400_BAD_REQUEST
        except Exception:
            ret = {
                'errors': 'Internal Error:' + traceback.format_exc(),
                'warnings':[]
                }
            rtn_status = status.HTTP_500_INTERNAL_SERVER_ERROR
       
        return Response (ret, status=rtn_status)
    
    def destroy(self, request, station_id, pk):
        form = Form.current_form(self.form_type_name, station_id)
        try:
            irf = FormData.find_object_by_id(pk, form)
        except ObjectDoesNotExist:
            return Response({'errors' : ["IRF not found"], 'warnings':[]}, status=status.HTTP_404_NOT_FOUND)
        
        if not UserLocationPermission.has_session_permission(request, 'IRF', 'DELETE', irf.station.operating_country.id, irf.station.id):
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        form_data = FormData(irf, form)
        form_data.delete()
        form_done.send_robust(sender=self.__class__, form_data=form_data, remove=True)
        return Response(status=status.HTTP_200_OK)

