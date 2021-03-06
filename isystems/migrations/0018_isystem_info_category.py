# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-26 01:53
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('isystems', '0017_auto_20170626_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='isystem',
            name='info_category',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('К', 'Конфиденциальная'), ('КТ', 'Коммерческая тайна'), ('ПДн', 'Персональные данные'), ('ДСП', 'Для служебного пользования')], default='', max_length=20, null=True, verbose_name='Категории обрабатываемой информации'),
        ),
    ]
