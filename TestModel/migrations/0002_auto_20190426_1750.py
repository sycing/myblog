# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-26 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u5206\u7c7b', 'verbose_name_plural': '\u5206\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': '\u8d26\u6237', 'verbose_name_plural': '\u8d26\u6237'},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-created_time'], 'verbose_name': '\u535a\u6587', 'verbose_name_plural': '\u535a\u6587'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '\u6807\u7b7e', 'verbose_name_plural': '\u6807\u7b7e'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='category',
            field=models.ManyToManyField(to='TestModel.Category', verbose_name='\u6982\u8981'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='TestModel.Tag', verbose_name='\u6807\u7b7e'),
        ),
    ]