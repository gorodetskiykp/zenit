# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-14 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_auto_20170208_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='ogrn',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='ОГРН'),
        ),
        migrations.AddField(
            model_name='organization',
            name='okpo',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='ОКПО'),
        ),
    ]
