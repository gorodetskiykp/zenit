# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-08 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_charts', '0002_auto_20170208_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='title',
            field=models.TextField(default='План-график', verbose_name='Название графика'),
        ),
    ]
