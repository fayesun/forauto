from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import MysqlReplFrom

# Create your views here.

class IndexView(TemplateView):
    template_name = 'mysqltools/index.html'


class ListReplView(TemplateView):
    template_name = 'mysqltools/listrepl.html'

class NewReplView(TemplateView):
    template_name = 'mysqltools/newrepl.html'