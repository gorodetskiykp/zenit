# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-15 02:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0007_auto_20170417_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_date', models.DateField(blank=True, null=True, verbose_name='Дата документа')),
                ('doc_name', models.CharField(default='', max_length=500, verbose_name='Название документа')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_documents', to='organizations.Organization', verbose_name='Создатель документа')),
            ],
            options={
                'ordering': ['doc_name'],
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='Document_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=150, verbose_name='Тип документа')),
            ],
            options={
                'ordering': ['type'],
                'verbose_name': 'Тип документа',
                'verbose_name_plural': 'Типы документов',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='doc_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type_documents', to='docs.Document_Type', verbose_name='Тип документа'),
        ),
    ]
