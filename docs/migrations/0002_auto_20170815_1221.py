# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-15 02:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document_type',
            options={'ordering': ['doc_type'], 'verbose_name': 'Тип документа', 'verbose_name_plural': 'Типы документов'},
        ),
        migrations.RenameField(
            model_name='document_type',
            old_name='type',
            new_name='doc_type',
        ),
    ]
