from __future__ import unicode_literals
from django.db import models
import os

class Package(models.Model):

	repository = models.URLField('url repositorio del proyecto', max_length=100, unique=True)
	name_package = models.CharField('nombre paquete', max_length=50, unique=True)
	description_package = models.CharField('descripcion paquete', max_length=50)
	email = models.EmailField('correo del postulador', max_length=50)
	#owner = models.ForeignKey('auth.User', related_name='packages')

	class Meta:
		ordering = ('name_package',)
			
	#Funcion para obtener el nombre del paquete mediante la URL
	def basename(self): 
		basename, extension = os.path.splitext(self.repository)
		return os.path.basename(basename)

	def __str__(self):
		return self.basename()

class Package_status(models.Model):

	package_id = models.ForeignKey(Package, on_delete=models.CASCADE)
	status = models.CharField('estatus del paquete', max_length=50, default='Recibido')

	class Meta:
		ordering = ('package_id',)
		
	def __str__(self):
		return self.package_id()
