from django import forms
from postulacion.models import Package

class PackageForm(forms.ModelForm):
	class Meta:
		model = Package
		fields = [
			"repository", 
			"name_package", 
			"description_package", 
			"email"
		]
		
		label={
			'repository':'Repositorio', 
			'name_package':'Nombre del Paquete', 
			'description_package':'Descripcion del Paquete', 
			'email':' Correo',
		}
		 
