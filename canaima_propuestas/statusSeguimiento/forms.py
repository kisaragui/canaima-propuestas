from django import forms
from statusSeguimiento.models import Historial

class HistorialForm(forms.ModelForm):
	class Meta:
		model = Historial
		fields = ["name_package", "status"]

