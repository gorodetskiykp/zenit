# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
        ('isystems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='isystem',
            name='developer',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='systems', to='organizations.Organization', verbose_name='Разработчик'),
        ),
    ]
