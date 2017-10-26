# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-26 00:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0013_people_info'),
        ('isystems', '0016_isystem_administrator'),
    ]

    operations = [
        migrations.AddField(
            model_name='isystem',
            name='contract_administrator',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_administrator_systems', to='people.Organization_Based_Role', verbose_name='Ответственный за договоры и бюджет'),
        ),
        migrations.AddField(
            model_name='isystem',
            name='isecurity_administrator',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='isecurity_administrator_systems', to='people.Organization_Based_Role', verbose_name='Ответственный за информационную безопасность'),
        ),
        migrations.AddField(
            model_name='isystem',
            name='reserve_administrator',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserve_administrator_systems', to='people.Organization_Based_Role', verbose_name='Резервный администратор'),
        ),
    ]