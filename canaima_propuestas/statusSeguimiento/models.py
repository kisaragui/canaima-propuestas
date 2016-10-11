from __future__ import unicode_literals
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import datetime
# Create your models here.

postulado = "p"
evaluado= "e"
aceptado= "a"
rechazado= "r"

STATUS=(
	(postulado,'postulado'),
	(evaluado,'evaluado'),
	(aceptado,'aceptado'),
	(rechazado,'rechazado'),
	)	
class Historial(models.Model):

	name_package = models.CharField('nombre paquete', max_length=50)
	fecha_actualizada = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=2, choices=STATUS, default=postulado)
	
	class Meta:
		ordering = ('fecha_actualizada',)
		

	def __str__(self):
		return self.name_package


	