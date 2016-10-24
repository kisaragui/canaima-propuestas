from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from statusSeguimiento.models import Historial

# funcion para guardar datos en el modelo Historial al guardar datos en el modelo Package
def guardar_historial(sender, instance, created, **kwargs):
	# cargando la instancia en el modelo Historial
	historial= Historial(name_package=instance.name_package)
	# guardando los datos instanciandos en el modelo Historial
	historial.save()

class Package(models.Model):

	repository = models.URLField('url repositorio del proyecto', max_length=150, unique=True)
	name_package = models.CharField('nombre paquete', max_length=50, unique=True)
	description_package = models.CharField('descripcion paquete', max_length=200, unique=True)
	status = models.CharField('estatus del paquete', max_length=50, default='postulado')
	email = models.EmailField('correo del postulador', max_length=50, unique=True)
	fecha = models.DateField('fecha de creacion del paquete', auto_now_add=True, auto_now=False)
	
	class Meta:
		ordering = ('name_package',)
			
	#def __str__(self):
	#	return self.basename()

# al guardar un dato en el modelo, dispara o envia esta Signal o Senial  para ejectutarla
post_save.connect(guardar_historial, sender=Package)
