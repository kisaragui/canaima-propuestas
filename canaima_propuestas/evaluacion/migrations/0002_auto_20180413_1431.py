# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-13 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion',
            name='comando_mal',
            field=models.CharField(blank=True, choices=[('SI', 'Si'), ('NO', 'No')], max_length=2),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='dependecia_adicional',
            field=models.CharField(blank=True, choices=[('SI', 'Si'), ('NO', 'No')], max_length=2),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='dev_doc_ejecucion',
            field=models.CharField(blank=True, choices=[('SI', 'Si'), ('NO', 'No')], max_length=2),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='firmado',
            field=models.CharField(blank=True, choices=[('SI', 'Si'), ('NO', 'No')], max_length=2),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='manual_usuario',
            field=models.CharField(blank=True, choices=[('SI', 'Si'), ('NO', 'No'), ('OT', 'Otro')], max_length=2),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='rama_desarrollo',
            field=models.CharField(blank=True, choices=[('main', 'Main'), ('contrib', 'Contrib'), ('non-free', 'Non-free')], max_length=8),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='readme',
            field=models.CharField(blank=True, choices=[('SI', 'Si'), ('NO', 'No')], max_length=2),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='tipo_doc',
            field=models.CharField(blank=True, choices=[('USU', 'Usuario'), ('DEV', 'Desarrollador'), ('OTO', 'Otro')], max_length=3),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='tipo_peso',
            field=models.CharField(blank=True, choices=[('PA', 'Paquete'), ('CF', 'Codigo-Fuente'), ('OT', 'Otro')], max_length=2),
        ),
    ]
