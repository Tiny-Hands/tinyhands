from django.contrib import admin
from dataentry.models import *


class InterceptionRecordAdmin(admin.ModelAdmin):
    model = InterceptionRecord
    search_fields = ['irf_number', 'staff_name']
    list_display = ['irf_number', 'staff_name', 'number_of_victims', 'number_of_traffickers', 'date_time_of_interception', 'date_time_entered_into_system', 'date_time_last_updated']


class VictimInterviewAdmin(admin.ModelAdmin):
    model = VictimInterview
    search_fields = ['vif_number', 'interviewer']
    list_display = ['vif_number', 'interviewer', 'number_of_victims', 'number_of_traffickers', 'date', 'date_time_entered_into_system', 'date_time_last_updated']


class DistrictAdmin(admin.ModelAdmin):
	model = District
	search_fields = ['name']
	list_display = ['name']

class IntercepteeAdmin(admin.ModelAdmin):
    model = Interceptee
    search_fields = ['canonical_name']
    list_display = ['canonical_name', 'id']

class PersonAdmin(admin.ModelAdmin):
    model = Interceptee
    search_fields = ['canonical_name']
    list_display = ['canonical_name', 'id']

class BorderStationAdmin(admin.ModelAdmin):
    model = BorderStation
    search_fields = ['station_name']
    list_display = ['station_name']

class VDCAdmin(admin.ModelAdmin):
	model = VDC
	search_fields = ['name','latitude','longitude','district','cannonical_name']
	list_display = ['name','latitude','longitude','district','cannonical_name']

admin.site.register(InterceptionRecord, InterceptionRecordAdmin)
admin.site.register(VictimInterview, VictimInterviewAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(BorderStation, BorderStationAdmin)
admin.site.register(Interceptee, IntercepteeAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(VDC, VDCAdmin)

