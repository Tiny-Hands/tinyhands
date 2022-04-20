from budget.pdfexports.pdf_creator import BasePDFCreator
from budget.helpers import MoneyDistributionFormHelper, Footnote
from dataentry.models import BorderStation
import zipfile
from io import BytesIO


class MDFExporter(BasePDFCreator):
    template_name = 'budget/MoneyDistributionTemplate.rml'

    def __init__(self, mdf):
        super(MDFExporter, self).__init__(self.template_name, self.get_mdf_data(mdf))

    def get_mdf_data(self, mdf):
        self.mdf_list = []
        first_page_footnote = Footnote()
        second_page_footnote = Footnote()
        impact_multiplying_list = BorderStation.objects.filter(
                operating_country=mdf.border_station.operating_country, project_category__name='Impact Multiplying')
        main_mdf_helper = MoneyDistributionFormHelper(mdf, mdf.border_station, first_page_footnote, second_page_footnote)
        distribution_subtotal = main_mdf_helper.total
        station_subtotal = main_mdf_helper.station_total
        self.mdf_list.append(main_mdf_helper)
        for impact_multiplying in impact_multiplying_list:
            impact_mdf = MoneyDistributionFormHelper(mdf, impact_multiplying, first_page_footnote, second_page_footnote)
            distribution_subtotal += impact_mdf.total
            station_subtotal += impact_mdf.station_total
            self.mdf_list.append(impact_mdf)
        return {
            'name': main_mdf_helper.station_name,
            'date': main_mdf_helper.date_entered,
            'month': main_mdf_helper.report_month,
            'mdfs':self.mdf_list,
            'first_footnotes': first_page_footnote,
            'second_footnotes': second_page_footnote,
            'distribution_subtotal': distribution_subtotal,
            'station_subtotal': station_subtotal,
            'other_detail': self.otherDetailPresent()
        }
    
    def otherDetailPresent(self):
        for mdf in self.mdf_list:
            if mdf.money_not_spent_data.has_data():
                return True
            if mdf.past_sent.has_data():
                return True
        
        return False


class MDFBulkExporter():
    def __init__(self, budgets):
        self.budgets = budgets

    def create(self):
        output = BytesIO()
        mdf_zip = zipfile.ZipFile(output, 'w')

        for budget in self.budgets:
            pdf = MDFExporter(budget).create()
            mdf_zip.writestr(budget.mdf_file_name(), pdf.getvalue())
        mdf_zip.close()
        
        return output
