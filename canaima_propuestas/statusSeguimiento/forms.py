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

        widgets = {'pre1': forms.RadioSelect}

class ObsEvaluadorForm(forms.ModelForm):

	class Meta:
		model = ObsEvaluador
		fields = ['obs1', 'obs2', 'obs3', 'obs4', 'obs5', 'obs6', 'obs7', 'obs8', 'obs9']


    
