from django.conf.urls import url, include
from xlsparse import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.parser_list, name='list_parser'),
    url(r'^upload/$', views.upload_file, name='upload'),
    url(r'^(?P<file_id>[0-9]+)/$', views.get_parser, name='parser'),



]
