# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(default='', max_length=250, verbose_name='Фамилия Имя Отчество')),
            ],
            options={
                'verbose_name': 'Человек',
                'ordering': ['fio'],
                'verbose_name_plural': 'Люди',
            },
        ),
    ]
