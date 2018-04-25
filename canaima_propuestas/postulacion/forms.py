from django import forms
from postulacion.models import Package
from captcha.fields import CaptchaField
from registration.forms import RegistrationForm
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class PackageForm(forms.ModelForm):

	captcha = CaptchaField()
	description_package = forms.CharField(label="Descripcion del paquete", widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))

	class Meta:
		model = Package
		fields = [
			"repository", 
			"name_package", 
			"description_package", 
		]
		exclude = [			
			"usuario",
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

class UsuarioCaptchaForm(RegistrationForm):

	bad_domains = ['aim.com', 'aol.com', 'email.com', 'gemail.com',
                   'googlemail.com', 'hushmail.com', 'mail.ru', 'mailinator.com', 
                   'live.com', 'correo.com', 'mail.com', 'latinmail.com']

	captcha = CaptchaField()
	
	def clean_email(self):

		email_domain = self.cleaned_data['email'].split('@')[1]
		if User.objects.filter(email__iexact=self.cleaned_data['email']):
			raise forms.ValidationError("Esta direccion de correo electronico ya esta en uso. Proporcione una direccion de correo electronico diferente.")
    
		if email_domain in self.bad_domains:
			raise forms.ValidationError("Su direccion de correo electronico no es valido. Por favor, proporcione una direccion de correo electronico diferente.")
		
		return self.cleaned_data['email']


	