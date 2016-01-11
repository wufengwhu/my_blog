from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from biportal.models import DataTransJobForm


class FormHorizontalView(FormView):
    template_name = 'data_trans_form_horizontal.html'
    form_class = DataTransJobForm

def big_trans(request):
    return render(request, 'big_trans.html')