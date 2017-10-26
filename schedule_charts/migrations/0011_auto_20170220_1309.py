# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-20 03:09
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_charts', '0010_auto_20170220_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='schedule_charts.Step', verbose_name='Родительский этап'),
        ),
    ]