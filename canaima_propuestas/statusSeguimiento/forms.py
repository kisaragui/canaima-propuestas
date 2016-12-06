from django import forms
from statusSeguimiento.models import Historial, PreEvaluador, ObsEvaluador

class HistorialForm(forms.ModelForm):
	class Meta:
		model = Historial
		fields = ["name_package", "status"]

class PreEvaluadorForm(forms.ModelForm):

    class Meta:
        model = PreEvaluador
        fields = ['pre1', 'pre2', 'pre3', 'pre4', 'pre5', 'pre6', 'pre7', 'pre8', 'pre9']

        widgets = {
        		'pre1': forms.CheckboxInput,
        		'pre2': forms.CheckboxInput,
        		'pre3': forms.CheckboxInput,
        		'pre4': forms.CheckboxInput,
        		'pre5': forms.CheckboxInput,
        		'pre6': forms.CheckboxInput,
        		'pre7': forms.CheckboxInput,
        		'pre8': forms.CheckboxInput,
        		'pre9': forms.CheckboxInput
        		}

class ObsEvaluadorForm(forms.ModelForm):

	class Meta:
		model = ObsEvaluador
		fields = ['obs1', 'obs2', 'obs3', 'obs4', 'obs5', 'obs6', 'obs7', 'obs8', 'obs9']


    
