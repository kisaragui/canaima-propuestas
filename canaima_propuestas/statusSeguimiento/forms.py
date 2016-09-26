from django import forms
from statusSeguimiento.models import Historial

class HistorialForm(forms.ModelForm):
	class Meta:
		model = Historial
		fields = [
			'name_package', 
			'status', 
		]
			
		label={
			'name_package':'Nombre del Paquete', 
			'status':'Status del Paquete', 
		}
		 
