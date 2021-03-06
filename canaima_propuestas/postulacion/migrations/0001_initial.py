# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-02 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50, verbose_name='Nombre de Usuario')),
                ('repository', models.URLField(max_length=150, unique=True, verbose_name='Direccion url del repositorio del paquete')),
                ('name_package', models.CharField(max_length=50, verbose_name='Nombre del paquete')),
                ('description_package', models.CharField(max_length=200, unique=True, verbose_name='Descripcion del paquete')),
                ('status', models.CharField(default='Postulado', max_length=50, verbose_name='Estatus del paquete')),
                ('email', models.EmailField(max_length=50, verbose_name='Correo del postulador')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion del paquete')),
            ],
        ),
    ]
