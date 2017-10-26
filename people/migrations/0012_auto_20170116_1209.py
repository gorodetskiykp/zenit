# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 02:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_auto_20170116_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system_based_role',
            name='people',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sys_roles', to='people.Organization_Based_Role', verbose_name='Работник'),
        ),
    ]