#coding:utf-8
import xadmin
from xadmin import views
from action_adminx import *


from .models import models,Contact,Category,Tag,Entry
class ContactAdmin(object):
    list_display = ['name', 'age','email']   #显示字段
    search_fields = ['name']  #搜索功能
    list_filter = ['name']    #过滤器
    actions=[MyAction,]
xadmin.site.register(Contact, ContactAdmin)

class CategoryAdmin(object):
    list_display=['name']
    search_fields=['name']
    list_filter=['name']
xadmin.site.register(Category,CategoryAdmin)

class TagAdmin(object):
    list_display=['name']
    search_fields = ['name']
    list_filter = ['name']
xadmin.site.register(Tag,TagAdmin)

class EntryAdmin(object):
    list_display = ['title','author','visiting','category','tags','created_time','modifyed_time']
    search_fields = ['title','author']
    list_filter = ['title','author','tags']
xadmin.site.register(Entry,EntryAdmin)

# 主题设置
class BaseSetting(object):
    # 打开主题功能
    enable_themes = True
    use_bootswatch = True

# 全局设置
class GlobalSettings(object):
    site_title = u"后台管理系统"  # 更改文字显示
    site_footer = u"LUIS博客管理系统"
    menu_style = u"accordion"   # 菜单收起
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

