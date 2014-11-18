from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
# from budget.models import InterceptionRecordListView
from accounts.mixins import PermissionsRequiredMixin
from budget.forms import BorderStationBudgetCalculationForm
from budget.models import BorderStationBudgetCalculation, OtherBudgetItemCost


class OtherBudgetItemCostFormInline(InlineFormSet):
    model = OtherBudgetItemCost


class BudgetCalcCreateView(
        LoginRequiredMixin,
        CreateWithInlinesView):
    model = BorderStationBudgetCalculation
    template_name = 'budget/budget_calculation_form.html'
    form_class = BorderStationBudgetCalculationForm
    success_url = reverse_lazy('home')
    inlines = [OtherBudgetItemCostFormInline]


class BudgetCalcListView(
        LoginRequiredMixin,
        ListView):
    model = BorderStationBudgetCalculation

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Template, Context

from z3c.rml import rml2pdf
from reportlab import *
import preppy
import cStringIO


def search_form(request):
    return render_to_response('search_form.html')


def getPDF(request):
    """Returns PDF as a binary stream."""

    if 'q' in request.GET:

        rml = getRML(request.GET['q'])

        buf = cStringIO.StringIO()

        #create the pdf
        rml2pdf.go(rml, outputFileName=buf)
        buf.reset()
        pdfData = buf.read()

        #send the response
        response = HttpResponse(mimetype='application/pdf')
        response.write(pdfData)
        response['Content-Disposition'] = 'attachment; filename=output.pdf'
        return response

def getRML(name):
    """We used django template to write the RML, but you could use any other
    template language of your choice.
    """
    t = Template(open('budget/templates/budget/test.rml').read())
    c = Context({"name": name})
    rml = t.render(c)
    #django templates are unicode, and so need to be encoded to utf-8
    return rml.encode('utf8')
