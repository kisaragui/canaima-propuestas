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

class PreEvaluador(models.Model):
	
	name = models.CharField(max_length= 50, blank=True)
	pre1 = models.BooleanField(max_length=5, choices=OPCION2, default=no)
	pre2 = models.BooleanField(max_length=5, choices=OPCION2, default=no)
	pre3 = models.BooleanField(max_length=5, choices=OPCION2, default=no)
	pre4 = models.BooleanField(max_length=5, choices=OPCION2, default=no)
	pre5 = models.BooleanField(max_length=5, choices=OPCION2, default=no)
	pre6 = models.BooleanField(max_length=5, choices=OPCION2, default=no)
	pre7 = models.BooleanField(max_length=5, choices=OPCION2, default=no)
	pre8_0 = models.BooleanField("main",max_length=7, choices=OPCION2, default=no)
	pre8_1 = models.BooleanField("contrib", max_length=7, choices=OPCION2, default=no)
	pre8_2 = models.BooleanField("non-free",max_length=7, choices=OPCION2, default=no)
	pre9 = models.BooleanField(max_length=5, choices=OPCION2, default=no)

class ObsEvaluador(models.Model):
	
	name = models.CharField( max_length= 50, blank=True)
	obs1 = models.CharField("Observaciones", max_length=200, blank=True)
	obs2 = models.CharField("Observaciones", max_length=200, blank=True)
	obs3 = models.CharField("Observaciones", max_length=200, blank=True)
	obs4 = models.CharField("Observaciones", max_length=200, blank=True)
	obs5 = models.CharField("Observaciones", max_length=200, blank=True)
	obs6 = models.CharField("Observaciones", max_length=200, blank=True)
	obs7 = models.CharField("Observaciones", max_length=200, blank=True)
	obs8 = models.CharField("Observaciones", max_length=200, blank=True)
	obs9 = models.CharField("Observaciones", max_length=200, blank=True)

	
			

	


	