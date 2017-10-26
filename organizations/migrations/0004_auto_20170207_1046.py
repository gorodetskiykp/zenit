# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-07 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_auto_20170203_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='official_info',
            field=models.URLField(blank=True, default='', null=True, verbose_name='Карточка организации'),
        ),
        migrations.AddField(
            model_name='organization',
            name='sites',
            field=models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Sites'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='ks',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='К/с №'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='rs',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Р/с №'),
        ),
    ]