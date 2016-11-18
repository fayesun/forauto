from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import MysqlReplFrom

# Create your views here.

class IndexView(TemplateView):
    template_name = 'mysqltools/index.html'


class ListReplView(TemplateView):
    template_name = 'mysqltools/listrepl.html'

class NewReplView(FormView):
    template_name = 'mysqltools/newrepl.html'
    form_class = MysqlReplFrom
    success_url = '/index/'