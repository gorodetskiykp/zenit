# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isystems', '0005_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='link_eatd',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на отчетный документ в ЭАТД'),
        ),
    ]
