# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-03 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postulacion', '0005_auto_20180402_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='description_package',
            field=models.CharField(max_length=200, unique=True, verbose_name='Descripcion del paquete'),
        ),
    ]
