from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from statusSeguimiento.models import Historial, PreEvaluador, ObsEvaluador
from django.utils import timezone
import datetime

# funcion para guardar datos en el modelo Historial al guardar datos en el modelo Package
def guardar_historial(sender, instance, created, **kwargs):
	# cargando la instancia en el modelo Historial
	historial= Historial(name_package=instance.name_package, status = instance.status)
	# guardando los datos instanciandos en el modelo Historial
	historial.save()

def guardarFormularioEvaluacion(sender, instance, created, **kwargs):
	preguntas = PreEvaluador(id=instance.id)
	preguntas.save()
	observacion = ObsEvaluador(id=instance.id)
	observacion.save()

class Package(models.Model):

	repository = models.URLField('Direccion url del repositorio del paquete', max_length=150, unique=True)
	name_package = models.CharField('Nombre del paquete', max_length=50, unique=True)
	description_package = models.CharField('Descripcion del paquete', max_length=200, unique=True)
	status = models.CharField('Estatus del paquete', max_length=50, default='Postulado')
	email = models.EmailField('Correo del postulador', max_length=50, unique=True)
	fecha = models.DateTimeField('fecha de creacion del paquete', auto_now_add=True, auto_now=False)
	
	class Meta:
		ordering = ('name_package',)
			
# al guardar un dato en el modelo, dispara o envia esta Signal o Senial  para ejectutarla
post_save.connect(guardar_historial, sender=Package)
post_save.connect(guardarFormularioEvaluacion, sender=Package)