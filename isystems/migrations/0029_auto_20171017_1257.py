# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-17 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isystems', '0028_auto_20171017_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='isystem',
            name='abbreviation',
            field=models.CharField(help_text='Латинскими прописными буквами, допускается символ подчеркивания', max_length=20, unique=True, verbose_name='Аббревиатура'),
        ),
        migrations.AlterField(
            model_name='isystem',
            name='full_name',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Полное название'),
        ),
        migrations.AlterField(
            model_name='isystem',
            name='short_name',
            field=models.CharField(default='', max_length=50, unique=True, verbose_name='Краткое название'),
        ),
    ]
