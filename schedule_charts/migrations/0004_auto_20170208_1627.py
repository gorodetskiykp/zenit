# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-08 06:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_charts', '0003_auto_20170208_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['schedule'], 'verbose_name': 'Этап', 'verbose_name_plural': 'Этапы'},
        ),
    ]
