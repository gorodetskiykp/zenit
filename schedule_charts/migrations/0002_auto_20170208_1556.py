# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-08 05:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_charts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_num', models.PositiveSmallIntegerField(blank=True, default='', null=True, verbose_name='Номер этапа')),
                ('title', models.TextField(default='', verbose_name='Этап')),
                ('date_begin', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('date_end', models.DateField(blank=True, null=True, verbose_name='Дата завершения')),
                ('status', models.BooleanField(default=False, verbose_name='Этап завершен')),
                ('parent_step', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='schedule_charts.Step', verbose_name='Родительский этап')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на скан в ЭАТД'),
        ),
        migrations.AddField(
            model_name='step',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='schedule_charts.Schedule', verbose_name='План-график'),
        ),
    ]