from django import forms
from postulacion.models import Package
from captcha.fields import CaptchaField

class PackageForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = Package
		fields = [
			"repository", 
			"name_package", 
			"description_package", 
			"email",
		]
		 
class UpdateForm(forms.ModelForm):
	class Meta:
		model = Package
		fields = ["name_package", "status"]

