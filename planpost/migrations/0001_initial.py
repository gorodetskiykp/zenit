# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default='20', max_length=4, verbose_name='Год')),
                ('status', models.CharField(choices=[('rdy', 'Утвержден в работу'), ('pro', 'Проект')], default='pro', max_length=3, verbose_name='статус')),
                ('ism_no', models.PositiveSmallIntegerField(default=0, verbose_name='Номер изм, если это изм')),
                ('base_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='planpost.Plan', verbose_name='Основной план, если это изм')),
            ],
            options={
                'verbose_name_plural': 'Планы поставок',
                'ordering': ['-year'],
                'verbose_name': 'План поставок',
            },
        ),
    ]
