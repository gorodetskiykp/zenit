# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-14 05:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0012_auto_20170116_1209'),
        ('organizations', '0005_auto_20170208_1556'),
        ('schedule_charts', '0005_auto_20170208_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutorOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='executor_orgs', to='organizations.Organization', verbose_name='Исполнитель')),
            ],
        ),
        migrations.AddField(
            model_name='step',
            name='man_executors',
            field=models.ManyToManyField(to='people.People', verbose_name='Исполнители'),
        ),
        migrations.AddField(
            model_name='step',
            name='org_executors',
            field=models.ManyToManyField(to='organizations.Organization', verbose_name='Исполнители'),
        ),
        migrations.AddField(
            model_name='step',
            name='repoper',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Подтверждающие документы'),
        ),
        migrations.AddField(
            model_name='executororg',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='executor_orgs', to='schedule_charts.Step', verbose_name='Этап'),
        ),
    ]
