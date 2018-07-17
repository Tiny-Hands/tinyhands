import json
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import filters as fs
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from braces.views import LoginRequiredMixin
from accounts.mixins import PermissionsRequiredMixin
import traceback
import json

from django.views.generic import CreateView
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import default_storage
from django.db import IntegrityError
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
from dataentry.serialize_form import FormDataSerializer
from dataentry.serializers import CountrySerializer

from dataentry.form_data import Form, FormData, FormType
from dataentry.models import BorderStation, Country, IrfCore, IrfNepal, UserLocationPermission

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
    date_time_of_interception = serializers.DateTimeField()
    date_time_entered_into_system = serializers.DateTimeField()
    date_time_last_updated = serializers.DateTimeField()
    station = BorderStationOverviewSerializer()
    can_view = serializers.SerializerMethodField(read_only=True)
    can_edit = serializers.SerializerMethodField(read_only=True)
    can_delete = serializers.SerializerMethodField(read_only=True)
    can_approve = serializers.SerializerMethodField(read_only=True)
    
    perm_group_name = 'IRF'
    
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
        #account_id = 10023
        
        #Get the account's IRF permissions and store them so they can be referenced by the serializer
        perm_list = UserLocationPermission.objects.filter(account__id=account_id, permission__permission_group=self.perm_group_name).exclude(permission__action='CREATE')
        self.serializer_context = {'perm_list':perm_list}
        
        # selected_countries to contain the list of country_ids where the user has VIEW permission for at
        # least one station
        selected_countries = []
        for perm in perm_list:
            if perm.country is None and perm.station is None:
                selected_countries = country_list
                break
            
            if perm.country is not None:
                id = perm.country.id
                if id in country_list and id not in selected_countries:
                    selected_countries.append(id)
            
            if perm.station is not None:
                id = perm.station.operating_country.id
                if id in country_list and id not in selected_countries:
                    selected_countries.append(id)
        
        # For each selected country where an IRF form exists, query the country IRF table
        # If VIEW permission is country wide, query all IRFs.  Otherwise query based on stations with VIEW permission
        queryset = None
        for country_id in all_country_list:
            form = Form.current_form(self.form_type_name, country_id)
            if form is not None:
                mod = __import__(form.storage.module_name, fromlist=[form.storage.form_model_name])
                form_model = getattr(mod, form.storage.form_model_name)
                
                if country_id in selected_countries:
                    filter_stations= []
                    country_perm_list = perm_list.filter(country=None, station=None)
                    country_perm_list = country_perm_list.union(perm_list.filter(country__id = country_id))
                    country_perm_list = country_perm_list.union(perm_list.filter(station__operating_country__id = country_id))
                    for perm in country_perm_list:
                        if perm.station is None:
                            filter_stations = []
                            break
                        else:
                            filter_stations.append(perm.station)
                        
                    if len(filter_stations):
                        tmp_queryset = form_model.objects.filter(station__in=filter_stations, status=status).only(
                            'id', 'irf_number', 'form_entered_by', 'number_of_victims', 'number_of_traffickers', 'staff_name', 
                            'station', 'date_time_of_interception', 'date_time_entered_into_system',
                            'date_time_last_updated')
                    else:
                        tmp_queryset = form_model.objects.filter(status=status).only(
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
        serializer = FormDataSerializer(data=request_json, context=self.serializer_context)
        if serializer.is_valid():
            if not UserLocationPermission.has_session_permission(request, 'IRF', 'ADD', serializer.get_country_id(), serializer.get_station_id()):
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            try:
                form_data = serializer.save()
            except IntegrityError as exc:
                if 'unique constraint' in exc.args[0]:
                    ret = {
                        'errors': [ exc.args[0] ],
                        'warnings':[]
                    }
                    return Response(ret, status=status.HTTP_400_BAD_REQUEST)
                else:
                    ret = {
                        'errors': [exc.args[0]],
                        'warnings':[]
                    }
                    return Response(ret, status=status.HTTP_400_BAD_REQUEST)
            serializer2 = FormDataSerializer(form_data, context=self.serializer_context)
            return Response(serializer2.data, status=status.HTTP_200_OK)
        else:
            ret = {
                'errors': serializer.the_errors,
                'warnings':serializer.the_warnings
                }
            return Response(ret, status=status.HTTP_400_BAD_REQUEST)
    
    def my_retrieve(self, request, country_id, pk):
        self.serializer_context = {}
        form = Form.current_form(self.form_type_name, country_id)
        try:
            irf = FormData.find_object_by_id(pk, form)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        read_access = UserLocationPermission.has_session_permission(request, 'IRF', 'VIEW', country_id, irf.station.id)
        edit_access = UserLocationPermission.has_session_permission(request, 'IRF', 'EDIT', country_id, irf.station.id)
        private_access = UserLocationPermission.has_session_permission(request, 'IRF', 'VIEW PI', country_id, irf.station.id)
        
        if not read_access:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
                
        if not edit_access and not private_access:
            self.serializer_context['mask_private'] = True
            
        form_data = FormData(irf, form)
        serializer = FormDataSerializer(form_data, context=self.serializer_context)
        
        resp_data = serializer.data
       
        return Response(resp_data)
    
    def update(self, request, country_id, pk):
        form = Form.current_form(self.form_type_name, country_id)
        irf = FormData.find_object_by_id(pk, form)
        if irf is None:
            return Response({'detail' : "IRF not found"}, status=status.HTTP_404_NOT_FOUND)
        form_data = FormData(irf, form)
        request_json = self.extract_data(request)

        self.serializer_context = {'form_type':form.form_type}
        serializer = FormDataSerializer(form_data, data=request_json, context=self.serializer_context)
        if serializer.is_valid():
            if not UserLocationPermission.has_session_permission(request, 'IRF', 'EDIT', serializer.get_country_id(), serializer.get_station_id()):
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            form_data = serializer.save()
            serializer2 = FormDataSerializer(form_data, context=self.serializer_context)
            return Response(serializer2.data, status=status.HTTP_200_OK)
        else:
            ret = {
                'errors': serializer.the_errors,
                'warnings':serializer.the_warnings
                }
            return Response(ret, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, country_id, pk):
        form = Form.current_form(self.form_type_name, country_id)
        try:
            irf = FormData.find_object_by_id(pk, form)
        except ObjectDoesNotExist:
            return Response({'detail' : "IRF not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if not UserLocationPermission.has_session_permission(request, 'IRF', 'DELETE', irf.station.operating_country.id, irf.station.id):
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        form_data = FormData(irf, form)
        form_data.delete()
        return Response(status=status.HTTP_200_OK)

