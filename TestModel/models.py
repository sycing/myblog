# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

#
# class Test(models.Model):
#     name = models.CharField(max_length=20)
#
#
class Contact(models.Model):
    name = models.CharField(u'名称',max_length=200)
    age = models.IntegerField(u'年龄',default=0)
    email = models.EmailField(u'邮箱')

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name='账户'
        verbose_name_plural=verbose_name




class Category(models.Model):
    name = models.CharField(u'名称',max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = verbose_name

class Tag(models.Model):
    name = models.CharField(u'标签', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name



class Entry(models.Model):
    # title=models.TextField(u'title')
    title = models.CharField('title',max_length=128)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='blog_img',null=True,blank=True)
    body = models.TextField('body')
    abstract = models.TextField('abstract',max_length=256,null=True,blank=True)
    visiting = models.PositiveIntegerField(u'visting',default=0)
    category = models.ManyToManyField('Category',verbose_name=u'概要')
    tags = models.ManyToManyField('Tag',verbose_name=u'标签')
    created_time = models.DateTimeField(u'创建时间',auto_now_add=True)
    modifyed_time = models.DateTimeField(u'更新时间',auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
        verbose_name = u'文章'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        # 获取当前博客详情页的url
        return reverse("blog:blog_detail", kwargs={"blog_id": self.id})  # app名字，详情页url的别名，参数是当前博客的id

    def increase_visiting(self):
        # 访问量加1
        self.visiting += 1
        self.save(update_fields=['visiting'])  # 只保存某个字段

