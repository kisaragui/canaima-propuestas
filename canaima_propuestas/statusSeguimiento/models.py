
from __future__ import unicode_literals
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import datetime
# Create your models here.

postulado = "postulado"
evaluado= "evaluado"
aceptado= "aceptado"
rechazado= "rechazado"

STATUS=(
	(postulado,'Postulado'),
	(evaluado,'En Evaluacion'),
	(aceptado,'Aceptado'),
	(rechazado,'Rechazado'),
	)	

OPCION2= ((True, "Yes"), (False, "No"),)
OPCION3= ((False, "main"), (False, "contrib"), (False, "non-free"),)

class Historial(models.Model):

	name_package = models.CharField('Nombre del Paquete', max_length=50)
	fecha_actualizada = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=10, choices=STATUS, default=evaluado)

	class Meta:
		ordering = ('fecha_actualizada',)
		
	def __str__(self):
		return self.name_package

class PreEvaluador(models.Model):
	name_package = models.ForeignKey(Historial, on_delete= models.CASCADE)
	pre1 = models.BooleanField(max_length=5, choices=OPCION2, default=False)
	pre2 = models.BooleanField(max_length=5, choices=OPCION2, default=False)
	pre3 = models.BooleanField(max_length=5, choices=OPCION2, default=False)
	pre4 = models.BooleanField(max_length=5, choices=OPCION2, default=False)
	pre5 = models.BooleanField(max_length=5, choices=OPCION2, default=False)
	pre6 = models.BooleanField(max_length=5, choices=OPCION2, default=False)
	pre7 = models.BooleanField(max_length=5, choices=OPCION2, default=False)
	pre8 = models.BooleanField(max_length=7, choices=OPCION3, default=False)
	pre9 = models.BooleanField(max_length=5, choices=OPCION2, default=False)

class ObsEvaluador(models.Model):
	pre = models.ForeignKey(PreEvaluador, on_delete= models.CASCADE)
	obs1 = models.CharField("Observaciones", max_length=200)
	obs2 = models.CharField("Observaciones", max_length=200)
	obs3 = models.CharField("Observaciones", max_length=200)
	obs4 = models.CharField("Observaciones", max_length=200)
	obs5 = models.CharField("Observaciones", max_length=200)
	obs6 = models.CharField("Observaciones", max_length=200)
	obs7 = models.CharField("Observaciones", max_length=200)
	obs8 = models.CharField("Observaciones", max_length=200)
	obs9 = models.CharField("Observaciones", max_length=200)

	

			

	


	