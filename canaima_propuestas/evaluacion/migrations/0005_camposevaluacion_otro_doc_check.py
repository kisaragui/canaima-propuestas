# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-27 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0004_auto_20180427_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='camposevaluacion',
            name='otro_doc_check',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
