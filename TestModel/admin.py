# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# from TestModel.models import Test,Contact,Tag
# Register your models here.
# class ContactAdmin(admin.ModelAdmin):
#     fields = ('name', 'email')
# admin.site.register(Contact, ContactAdmin)
# admin.site.register([Test, Tag])


from . import models

class EntryAdmin(admin.ModelAdmin):
    list_display = ['title','author','visiting','created_time','modifyed_time']


admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Entry,EntryAdmin)