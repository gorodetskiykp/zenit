# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-17 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0008_auto_20170417_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='ogrn',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='ОГРН'),
        ),
    ]