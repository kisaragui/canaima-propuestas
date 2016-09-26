from __future__ import unicode_literals
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

OPTIONS_CHOICES=(
	('postulado','postulado'),
	('evaluado','evaluado'),
	('aceptado','aceptado'),
	('rechazado','rechazado'),
	)	
class Historial(models.Model):

	name_package = models.CharField('nombre paquete', max_length=50, unique=True)
	fecha_actualizada = models.DateTimeField('fecha para actualizar del paquete', auto_now=True)
	status = models.CharField(max_length=50, choices=OPTIONS_CHOICES, default='postulado')
	
	class Meta:
		ordering = ('fecha_actualizada',)
		

	def __str__(self):
		return self.name_package()


	