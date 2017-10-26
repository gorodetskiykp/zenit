# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-03 05:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(default='', max_length=50, verbose_name='Тип адреса')),
            ],
        ),
        migrations.CreateModel(
            name='OrgAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('address_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='organizations.AddressType', verbose_name='Тип адреса')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='organizations.Organization', verbose_name='Организация')),
            ],
        ),
    ]