from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
# Create your models here.

	
postulado = "Postulado"
evaluado= "En Evaluacion"
aceptado= "Aceptado"
rechazado= "Rechazado"

STATUS=(
	(postulado,'Postulado'),
	(evaluado,'En Evaluacion'),
	(aceptado,'Aceptado'),
	(rechazado,'Rechazado'),
	)	
si = True
no = False

OPCION2= ((si, "Si"), (no, "No"),)

class Historial(models.Model):

	name_package = models.CharField('Nombre del Paquete', max_length=50)
	fecha_actualizada = models.DateTimeField(auto_now_add=True, auto_now=False)
	status = models.CharField(max_length=10, choices=STATUS, default=evaluado)

	class Meta:
		ordering = ('fecha_actualizada',)
		
	def __str__(self):
		return '%s %s' % (self.name_package, self.status)
	