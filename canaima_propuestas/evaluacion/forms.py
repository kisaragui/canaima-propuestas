# -*- coding: utf-8 -*-
from django import forms
from postulacion.forms import PackageForm
from postulacion.models import Package
from evaluacion.models import CamposEvaluacion

class PackageNoEditableForm(forms.ModelForm): 
	# Seccion 1 Identificacion del paquete

	def __init__(self, *args, **kwargs):
	 	super(PackageForm, self).__init__(*args, **kwargs)
	 	# itera cada uno de los campos del modelo
	 	for field in self.fields.values():
	 		# deshabilita los campos, para solo poder leerlos como "read only".
	 		field.disabled = True
		
	class Meta:

		model = Package
		fields = [ 
			"name_package",
			"usuario",
			"email",
			"description_package",
			"repository",
		]

class EvaluacionForm(forms.ModelForm): 

	OPCION = (("SI", "Si"), ("NO", "No"),)

	OPCION1 = (("SI", "Si"), ("NO", "No"), ("OT","Otro"))

	OPCION2 = (('main', 'Main'), ('contrib', 'Contrib'), ('non-free', 'Non-free'))

	OPCION3 = (('PA', 'Paquete'), ('CF', 'Codigo-Fuente'), ('OT', 'Otro'))

	OPCION4 = (('USU', 'Usuario'), ('DEV', 'Desarrollador'), ('OTRO', 'Otro'))
	
	# Seccion 2 llave GnuPG
	firmado = forms.MultipleChoiceField(choices=OPCION, label='Esta firmado',widget=forms.CheckboxSelectMultiple(), required=False)
	tipo_llave = forms.CharField(label='Tipo de llave')
	observacion2 = forms.CharField(label='Observaciones (opcional)', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
	# Seccion 3 Peso del paquete
	contenido_repo = forms.ChoiceField(choices=OPCION3, label='Contenido del repositorio', widget=forms.Select(attrs={'class': 'browser-default'}))
	cantidad = forms.CharField(label='Cantidad')
	observacion3 = forms.CharField(label='Observaciones (opcional)', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
	# Seccion 4 Empaquetamiento
	descripcion4 = forms.CharField(label="Descripción", widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
	# Seccion 5 Errores de lintian
	descripcion5 = forms.CharField(label="Descripción", widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
	# Seccion 6 Documentación
	readme = forms.ChoiceField(choices=OPCION, label='Posee README.md', widget=forms.CheckboxSelectMultiple(), required=False)
	otro_doc = forms.CharField(label='Otro Documento')
	tipo_doc = forms.ChoiceField(choices=OPCION4, label="Orientacion de la documentacion", widget=forms.Select(attrs={'class': 'browser-default'}))
	usu_usuario_check = forms.BooleanField(label="Usuario", required=False)
	usu_descripcion_check = forms.BooleanField(label="Descripción", required=False)
	dev_doc_ejecucion = forms.ChoiceField(choices=OPCION, label="Instrucciones para ejecutarse: ", widget=forms.CheckboxSelectMultiple(), required=False)
	otro_doc_check = forms.CharField(label='Especificación')
	lenguaje_programacion = forms.CharField(label="lenguajes de programación")
	manual_usuario = forms.ChoiceField(choices=OPCION1, label="Posee manual de usuario", widget=forms.CheckboxSelectMultiple(), required=False)
	otro_manual_usuario_check = forms.CharField(label='Especificación')
	dependecia_adicional = forms.ChoiceField(choices=OPCION, label="Libreria o dependencia adicional", widget=forms.CheckboxSelectMultiple(), required=False)
	dependecia_adicional_descripcion = forms.CharField(label="Describa (en caso si)", widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
	observacion6 = forms.CharField(label='Observaciones (opcional)', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
	# Seccion 7 Comando maliciosos
	comando_mal = forms.ChoiceField(choices=OPCION, label="En rasgos generales, posee comando malicioso o poco comunes", widget=forms.CheckboxSelectMultiple(), required=False)
	descripcion7 = forms.CharField(label='Describa (en caso si)', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
	# Seccion 8 Rama de desarrollo
	rama_desarrollo = forms.ChoiceField(choices=OPCION2, label="Rama de desarrollo sugerida", widget=forms.CheckboxSelectMultiple(), required=False)	
	observacion8 = forms.CharField(label='Observaciones (opcional)', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))

	class Meta:

		model = CamposEvaluacion
		fields = [
			"firmado",
			"tipo_llave",
			"observacion2",
			"contenido_repo",
			"cantidad",
			"observacion3",
			"despcricion4",
			"despcricion5",
			"readme",
			"otro_doc",
			"tipo_doc",
			"usu_usuario_check",
			"usu_descripcion_check",
			"otro_doc_check",
			"dev_doc_ejecucion",
			"lenguaje_programacion",
			"dependecia_adicional",
			"dependecia_adicional_descripcion",
			"manual_usuario",
			"otro_manual_usuario_check",
			"observacion6",
			"comando_mal",
			"descripcion",
			"rama_desarrollo",
			"observacion8",
		]















