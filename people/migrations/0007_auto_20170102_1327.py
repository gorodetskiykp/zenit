# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 03:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_people_organization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='people',
            name='post',
        ),
    ]
