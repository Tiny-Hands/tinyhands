from django.conf import settings

from dataentry.dataentry_signals import background_form_done
from dataentry.models import BorderStation
from budget.models import MonthlyDistributionForm, ProjectRequest, MdfItem
import budget.mdf_constants as constants
from export_import.google_sheet import GoogleSheet

def get_mdf_rows(mdfs):
    country_id = mdfs[0]["country_id"]
    year_month = mdfs[0]["year_month"]
    key = str(year_month) + '-' + str(country_id)
    
    line_item = {}
    for pair in constants.CATEGORY_CHOICES:
        line_item[pair[0]] = pair[1]
   
    mdfs = MonthlyDistributionForm.objects.filter(border_station__operating_country__id=country_id, status='Approved', 
                                                  month_year__year = year_month//100, month_year__month = year_month % 100)
    rows = [['Key', 'Year Month', 'Project', 'MDF Project', 'Line Item', 'Amount']]
    for mdf in mdfs:
        request_projects = list(ProjectRequest.objects.filter(monthlydistributionform=mdf).values_list('project__id', flat=True).distinct())
        item_projects = list(MdfItem.objects.filter(mdf=mdf).values_list('work_project__id', flat=True).distinct())
        project_ids = set(request_projects + item_projects)
        for project_id in project_ids:
            project = BorderStation.objects.get(id=project_id)
            if project_id == mdf.border_station.id:
                rows.append([key, year_month, project.station_code, mdf.border_station.station_code, line_item[constants.STAFF_BENEFITS], mdf.salary_and_benefits_total(project)])
                rows.append([key, year_month, project.station_code, mdf.border_station.station_code, line_item[constants.RENT_UTILITIES], mdf.rent_and_utilities_total()])
                rows.append([key, year_month, project.station_code, mdf.border_station.station_code, line_item[constants.ADMINISTRATION], mdf.administration_total()])
                rows.append([key, year_month, project.station_code, mdf.border_station.station_code, line_item[constants.AWARENESS], mdf.awareness_total()])
                rows.append([key, year_month, project.station_code, mdf.border_station.station_code, line_item[constants.TRAVEL], mdf.travel_total()])
                rows.append([key, year_month, project.station_code, mdf.border_station.station_code, line_item[constants.POTENTIAL_VICTIM_CARE], mdf.pv_total()])
                rows.append([key, year_month, project.station_code, mdf.border_station.station_code, line_item[constants.PAST_MONTH_SENT], mdf.past_month_sent_total(project)])
                rows.append([key, year_month, project.station_code, mdf.border_station.station_code, line_item[constants.MONEY_NOT_SPENT], mdf.money_not_spent_to_deduct_total(project)]) 
                rows.append([key, year_month, project.station_code, mdf.border_station.station_code, 'Total', mdf.distribution_total(project)])  
            else:
                rows.append([key, year_month, project.station_code, mdf.border_station.station_code, line_item[constants.STAFF_BENEFITS], mdf.salary_and_benefits_total(project)])
                rows.append([key, year_month, project.station_code, mdf.border_station.station_code, line_item[constants.IMPACT_MULTIPLYING], mdf.impact_multiplying_total(project)])
                rows.append([key, year_month, project.station_code, mdf.border_station.station_code, line_item[constants.PAST_MONTH_SENT], mdf.past_month_sent_total(project)])
                rows.append([key, year_month, project.station_code, mdf.border_station.station_code, line_item[constants.MONEY_NOT_SPENT], mdf.money_not_spent_to_deduct_total(project)])  
                rows.append([key, year_month, project.station_code, mdf.border_station.station_code, 'Total', mdf.distribution_total(project)]) 
    
    return rows

def export_country_mdf(sender, **kwargs):
    form_data = kwargs.get("form_data")
    if not ("mdf_export" in form_data):
        return
    
    country_id =form_data["country_id"]
    year_month = form_data["year_month"]
    key = str(year_month) + '-' + str(country_id)
    
    sheet = GoogleSheet("MDF" + settings.SPREADSHEET_SUFFIX, 'mdf', "Key", get_mdf_rows)
    sheet.update(key, form_data)
        

background_form_done.connect(export_country_mdf, weak=False, dispatch_uid="BackgroundFormWork")