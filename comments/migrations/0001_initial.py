# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-30 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TestModel', '0003_auto_20190428_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u7528\u6237\u540d')),
                ('email', models.EmailField(max_length=255, verbose_name='\u90ae\u7bb1')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u8bc4\u8bba\u65f6\u95f4')),
                ('repley_name', models.CharField(max_length=100, verbose_name='\u76ee\u6807\u7528\u6237')),
                ('ip_addr', models.CharField(max_length=100, verbose_name='ip\u5730\u5740')),
                ('message', models.CharField(max_length=200, verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('article_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestModel.Entry')),
            ],
        ),
    ]