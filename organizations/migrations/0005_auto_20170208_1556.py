# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-08 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_auto_20170207_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='emails',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='emails'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='sites',
            field=models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Сайт'),
        ),
    ]
