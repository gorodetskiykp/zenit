# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-03 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_addresstype_orgaddress'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addresstype',
            options={'verbose_name': 'Тип адреса', 'verbose_name_plural': 'Типы адресов'},
        ),
        migrations.AlterModelOptions(
            name='orgaddress',
            options={'verbose_name': 'Адрес', 'verbose_name_plural': 'Адреса'},
        ),
        migrations.AddField(
            model_name='organization',
            name='bik',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='БИК'),
        ),
        migrations.AddField(
            model_name='organization',
            name='emails',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Emails'),
        ),
        migrations.AddField(
            model_name='organization',
            name='faxes',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Факсы'),
        ),
        migrations.AddField(
            model_name='organization',
            name='inn',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='ИНН'),
        ),
        migrations.AddField(
            model_name='organization',
            name='kpp',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='КПП'),
        ),
        migrations.AddField(
            model_name='organization',
            name='ks',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='К/с'),
        ),
        migrations.AddField(
            model_name='organization',
            name='phones',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Телефоны'),
        ),
        migrations.AddField(
            model_name='organization',
            name='rs',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Р/с'),
        ),
    ]