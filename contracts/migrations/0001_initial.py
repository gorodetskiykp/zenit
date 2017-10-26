# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sed_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Внутренний номер')),
                ('reg_date', models.DateField(verbose_name='Дата регистрации')),
                ('ext_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Номер контрагента')),
                ('sed_project_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Проектный номер')),
                ('sed_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ссылка в СЭД')),
                ('title', models.TextField(verbose_name='Содержание')),
                ('contractor', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='organizations.Organization', verbose_name='Контрагент')),
            ],
            options={
                'verbose_name_plural': 'Договоры',
                'verbose_name': 'Договор',
                'ordering': ['reg_date', 'title'],
            },
        ),
    ]