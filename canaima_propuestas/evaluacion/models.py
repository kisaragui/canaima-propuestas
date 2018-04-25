# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from postulacion.models import Package
from django.db import models

# Create your models here.

# casillas o selects  

OPCION = (("SI", "Si"), ("NO", "No"))

OPCION1 = (("SI", "Si"), ("NO", "No"), ("OT","Otro"))

OPCION2 = (('main', 'Main'), ('contrib', 'Contrib'), ('non-free', 'Non-free'))

OPCION3 = (('PA', 'Paquete'), ('CF', 'Codigo-Fuente'), ('OT', 'Otro'))

OPCION4 = (('USU', 'Usuario'), ('DEV', 'Desarrollador'), ('OTO', 'Otro'))

class CamposEvaluacion(models.Model):


	# Seccion 1 Identificacion del paquete
	datos_paquete = models.OneToOneField(Package, on_delete=models.CASCADE)
	# Seccion 2 llave GnuPG
	firmado = models.CharField(choices=OPCION, max_length=2, blank=True)
	tipo_llave = models.CharField(max_length=50, blank=True)
	observacion2 = models.CharField(max_length=255, blank=True)
	# Seccion 3 Peso del paquete
	contenido_repo = models.CharField(choices=OPCION3, max_length=2, blank=True)
	cantidad_paquete = models.CharField(max_length=50, blank=True)
	cantidad_codigo = models.CharField(max_length=50, blank=True)
	cantidad_otro = models.CharField(max_length=50, blank=True)
	observacion3 = models.CharField(max_length=255, blank=True)
	# Seccion 4 Empaquetamiento
	despcricion4 = models.TextField(max_length=1000, blank=True)
	# Seccion 5 Errores de lintian
	despcricion5 = models.TextField(max_length=1000, blank=True)
	# Seccion 6 Documentación
	readme = models.CharField(choices=OPCION, max_length=2, blank=True)
	otro_doc = models.CharField(max_length=100, blank=True)
	tipo_doc = models.CharField(choices=OPCION4, max_length=3, blank=True)
	usu_usuario_check = models.BooleanField(default=False)
	usu_descripcion_check = models.BooleanField(default=False)
	dev_doc_ejecucion = models.CharField(choices=OPCION, max_length=2, blank=True)
	lenguaje_programacion = models.CharField(max_length=200, blank=True)
	dependecia_adicional = models.CharField(choices=OPCION, max_length=2, blank=True)
	dependecia_adicional_descripcion = models.CharField(max_length=255, blank=True)
	manual_usuario = models.CharField(choices=OPCION1, max_length=2, blank=True)
	observacion6 = models.CharField(max_length=255, blank=True)
	# Seccion 7 Comando maliciosos
	comando_mal = models.CharField(choices=OPCION, max_length=2, blank=True)
	descripcion = models.TextField(max_length=500, blank=True)
	# Seccion 8 Rama de desarrollo
	rama_desarrollo = models.CharField(choices=OPCION2, max_length=8, blank=True)
	observacion8 = models.CharField(max_length=255, blank=True)
	def __str__(self):
		return self.datos_paquete
		