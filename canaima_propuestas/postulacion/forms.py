from django import forms
from postulacion.models import Package
from captcha.fields import CaptchaField
from registration.forms import RegistrationFormUniqueEmail
import re
from django.core.exceptions import ValidationError

class PackageForm(forms.ModelForm):

	#captcha = CaptchaField()

	class Meta:
		model = Package
		fields = [
			"repository", 
			"name_package", 
			"description_package", 
			"email",
		]

	def clean_name_package(self):

		n = self.cleaned_data["name_package"]
		if  re.search(r"^[\w.@+-]*$", n) is None: 
			raise ValidationError('El nombre del paquete no tiene un nombre valido. los catacteres permitidos son letras, digitos y @/./+/-/_ solamente.')
		return self.cleaned_data["name_package"]

class UpdateForm(forms.ModelForm):
	class Meta:
		model = Package
		fields = ["name_package", "status"]

class EmailycaptchaForm(RegistrationFormUniqueEmail):

	#captcha = CaptchaField()
	
	pass

class Captcha(forms.Form):

	captcha = CaptchaField()

	