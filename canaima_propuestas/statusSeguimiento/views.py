from django.shortcuts import render
from statusSeguimiento.models import Historial, PreEvaluador, ObsEvaluador
from postulacion.models import Package
from django.views.generic import ListView, TemplateView
from django.core.urlresolvers import reverse_lazy
from statusSeguimiento.forms import HistorialForm, PreEvaluadorForm, ObsEvaluadorForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
# Create your views here.

class HistorialLista(ListView):
 
	model = Historial
	template_name = "lista_todo.html"


class Principal(TemplateView):
    template_name = "index.html"

