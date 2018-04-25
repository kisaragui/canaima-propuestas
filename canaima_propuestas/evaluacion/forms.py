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

	OPCION4 = (('USU', 'Usuario'), ('DEV', 'Desarrollador'), ('OTO', 'Otro'))
	
	# Seccion 2 llave GnuPG
	firmado = forms.MultipleChoiceField(choices=OPCION, label='Esta firmado',widget=forms.CheckboxSelectMultiple(), required=False)
	tipo_llave = forms.CharField(label='Tipo de llave')
	observacion2 = forms.CharField(label='Observaciones (opcional)', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
	# Seccion 3 Peso del paquete
	contenido_repo = forms.ChoiceField(choices=OPCION3, label='Contenido del repositorio', widget=forms.Select(attrs={'class': 'browser-default'}))
	cantidad_paquete = forms.CharField(label='Cantidad')
	cantidad_codigo = forms.CharField(label='Cantidad')
	cantidad_otro = forms.CharField(label='Cantidad')
	observacion3 = forms.CharField(label='Observaciones (opcional)', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
	# Seccion 4 Empaquetamiento
	despcricion4 = forms.CharField(label="Descripcion del paquete", widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
	# Seccion 5 Errores de lintian
	despcricion5 = forms.CharField(label="Descripcion del paquete", widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
	# Seccion 6 Documentacion
	readme = forms.ChoiceField(label='Posee README.md',widget=forms.CheckboxInput)
	otro_doc = forms.CharField(label='Otro Documento')
	tipo_doc = forms.CharField(label="Orientacion de la documentacion", widget=forms.RadioSelect)
	usu_usuario_check = forms.BooleanField(label="Caso Usuario, confirmacion de documentacion del paquete", widget=forms.CheckboxInput)
	usu_descripcion_check = forms.BooleanField(label="Caso Usuario, confirmacion de documentacion del paquete", widget=forms.CheckboxInput)
	dev_doc_ejecucion = forms.CharField(label="Caso desarrollador, confirmacion de documentacion del paquete")
	lenguaje_programacion = forms.CharField(label="lenguajes de programacion")
	dependecia_adicional = forms.ChoiceField(label="Libreria o dependencia adicional", widget=forms.CheckboxInput)
	dependecia_adicional_descripcion = forms.CharField(label="Describa (en caso si)", widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
	manual_usuario = forms.ChoiceField(label="Posee manual de usuario")
	observacion6 = forms.CharField(label='Observaciones (opcional)', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
	# Seccion 7 Comando maliciosos
	comando_mal = forms.CharField(label="En rasgos generales  posee comando maliciosos o poco comunes", widget=forms.CheckboxInput)
	descripcion = forms.CharField(label='Describa (en caso si)', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
	# Seccion 8 Rama de desarrollo
	rama_desarrollo = forms.CharField(label="Rama de desarrollo sugerida", widget=forms.CheckboxInput)	
	observacion8 = forms.CharField(label='Observaciones (opcional)', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))

	class Meta:

		model = CamposEvaluacion
		fields = [
			#"datos_paquete",
			"firmado",
			"tipo_llave",
			"observacion2",
			"contenido_repo",
			"cantidad_paquete",
			"cantidad_codigo",
			"cantidad_otro",
			"observacion3",
			"despcricion4",
			"despcricion5",
			"readme",
			"otro_doc",
			"tipo_doc",
			"usu_usuario_check",
			"usu_descripcion_check",
			"dev_doc_ejecucion",
			"lenguaje_programacion",
			"dependecia_adicional",
			"dependecia_adicional_descripcion",
			"manual_usuario",
			"observacion6",
			"comando_mal",
			"descripcion",
			"rama_desarrollo",
			"observacion8",
		]















