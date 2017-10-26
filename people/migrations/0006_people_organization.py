# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 16:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
        ('people', '0005_remove_people_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='organization',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people', to='organizations.Organization', verbose_name='Организация'),
        ),
    ]