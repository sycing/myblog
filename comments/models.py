# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from TestModel.models import *

# Create your models here.


class Comment(models.Model):
    name=models.CharField(u'用户名',max_length=50)
    email=models.EmailField(u'邮箱',max_length=255)
    create_time=models.DateTimeField(u'评论时间',auto_now_add=True)
    repley_name=models.CharField(u'目标用户',max_length=100)
    ip_addr=models.CharField(u'ip地址',max_length=100)
    message=models.CharField(u'评论内容',max_length=200)
    article_post=models.ForeignKey('TestModel.Entry',on_delete=models.CASCADE)

    def __str__(self):
        return self.message[:20]


