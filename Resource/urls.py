# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
from TestModel import views as blog_views

app_name='resource'

urlpatterns = [
    url(r'^$', views.index,name='resource_index'),
]