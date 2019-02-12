from django.shortcuts import render
from statusSeguimiento.models import Historial
from postulacion.models import Package
from django.views.generic import ListView, TemplateView
from django.core.urlresolvers import reverse_lazy
from statusSeguimiento.forms import HistorialForm
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

class HistorialLista(ListView):
 
	model = Historial
	template_name = "lista_todo.html"


class Principal(TemplateView):
    template_name = "index.html"

