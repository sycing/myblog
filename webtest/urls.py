# -*- coding: utf-8 -*-
"""webtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as static_serve  # 注意这里引入的与上面的不同

from TestModel import views as blog_views
from TestModel.feed import LatestEntriesFeed
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from TestModel.models import Entry

import xadmin
# # Uncomment the next two lines to enable the admin:
# xadmin.autodiscover()
# # version模块自动注册需要版本控制的 Model
# from xadmin.plugins import xversion
# xversion.register_models()


info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'modifyed_time'
}

urlpatterns = [
    url(r'^$',blog_views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^blog/',include('TestModel.urls') ),
    url(r'^resource/',include('Resource.urls')),
    url(r'^latest/feed/$', LatestEntriesFeed()),    #RSS订阅

    url(r'^media/(?P<path>.*)$' , static_serve, { 'document_root' : settings.MEDIA_ROOT}),#静态文件
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),  #站点地图

    # url(r'^comments/', include('django_comments.urls')),

    url(r'^comments/',include('comments.urls'))


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )


handler403 = blog_views.permission_denied
handler404 = blog_views.page_not_found
handler500 = blog_views.page_error