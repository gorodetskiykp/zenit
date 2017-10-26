# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-16 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isystems', '0025_auto_20170815_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='isystem',
            name='recovery_order',
            field=models.TextField(blank=True, null=True, verbose_name='Порядок восстановления'),
        ),
        migrations.AddField(
            model_name='isystem',
            name='test_procedure',
            field=models.TextField(blank=True, null=True, verbose_name='Порядок тестирования'),
        ),
        migrations.AddField(
            model_name='isystem',
            name='upgrade_order',
            field=models.TextField(blank=True, null=True, verbose_name='Порядок обновления'),
        ),
    ]
