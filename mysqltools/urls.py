from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^list-repl/$', views.ListReplView.as_view(), name='list-repl'),
    url(r'^new-repl/$', views.NewReplView.as_view(), name='new-repl'),
]