import pytz

from rest_framework import serializers
from rest_framework import filters as fs
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from dataentry.serialize_form import FormDataSerializer
from .base_form import BaseFormViewSet, BorderStationOverviewSerializer

from dataentry.form_data import Form, FormData
from dataentry.models import VdfNepal

class VdfListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    vdf_number = serializers.CharField()
    staff_name = serializers.CharField()
    date_of_interview = serializers.SerializerMethodField(read_only=True)
    date_time_entered_into_system = serializers.SerializerMethodField(read_only=True)
    date_time_last_updated = serializers.SerializerMethodField(read_only=True)
    station = BorderStationOverviewSerializer()
    form_name = serializers.SerializerMethodField(read_only=True)
    
    perm_group_name = 'VDF'
    
    def adjust_date_time_for_tz(self, date_time, tz_name):
        tz = pytz.timezone(tz_name)
        date_time = date_time.astimezone(tz)
        date_time = date_time.replace(microsecond=0)
        date_time = date_time.replace(tzinfo=None)
        return str(date_time)
    
    def get_date_of_interview(self, obj):
        return str(obj.interview_date.year) + '-' + str(obj.interview_date.month) + '-' + str(obj.interview_date.day)
    
    def get_date_time_entered_into_system(self, obj):
        return self.adjust_date_time_for_tz (obj.date_time_entered_into_system, obj.station.time_zone)
    
    def get_date_time_last_updated(self, obj):
        return self.adjust_date_time_for_tz (obj.date_time_last_updated, obj.station.time_zone)
    
    def get_form_name(self, obj):
        forms = Form.objects.filter(form_type__name='VDF', stations__id=obj.station.id)
        if len(forms) > 0:
            return forms[0].form_name
        else:
            return None
    
class VdfFormViewSet(BaseFormViewSet):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    permission_classes = (IsAuthenticated, )
    serializer_class = VdfListSerializer
    filter_backends = (fs.SearchFilter, fs.OrderingFilter,)
    search_fields = ('vdf_number',)
    ordering_fields = [
        'id', 'vdf_number', 'form_entered_by', 'staff_name', 
        'station', 'interview_date', 'date_time_entered_into_system',
        'date_time_last_updated']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return VdfListSerializer
        else:
            return FormDataSerializer
    
    def get_serializer_context(self): 
        return self.serializer_context
    
    def get_perm_group_name(self):
        return 'VDF'
    
    def get_form_type_name(self):
        return 'VDF'
    
    def get_element_paths(self):
        return [
            {
                'element':'scanned',
                'path':'vdf_attachments/'
            }]
    
    def get_list_field_names(self):
        return ['id', 'vdf_number', 'form_entered_by', 'staff_name', 
                'station', 'interview_date', 'date_time_entered_into_system',
                'date_time_last_updated']
        
    def get_empty_queryset(self):
        return VdfNepal.objects.none()
    
    def filter_key(self, queryset, search):
        return queryset.filter(vdf_number__contains=search)

