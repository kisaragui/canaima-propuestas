from django.shortcuts import get_object_or_404, render
from statusSeguimiento.models import Historial
from postulacion.models import Package
from django.views.generic import CreateView, ListView, UpdateView, DetailView, FormView
from django.views.generic.edit import ProcessFormView, FormMixin
from django.core.urlresolvers import reverse_lazy
from statusSeguimiento.forms import HistorialForm
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

class HistorialList(ListView, ProcessFormView, FormMixin):

	# lista los paquetes
	template_name="listar_status.html"
	model = Historial
	form_class = HistorialForm
	success_url = reverse_lazy("listar_todo")
	#context_object_name = 'package_list'	


	def post(self, request, *args, **kwargs):
		#almacenando en variables los datos enviandos por via POST
		s = request.POST["status"]
		n = request.POST["name_package"]
		form = self.form_class({'name_package':n,'status':s})
		
		if form.is_valid():
			print form
			return HttpResponse("listar_todo")
		else:
			return HttpResponse("listar_todo")	
		
		
		# validando los datos a actualizar
		#if form.is_valid():
		#	traza = form.save(commit=False)
		#	traza.name_package= request.POST["name_package"]
		#	traza.status= request.POST["status"]
		#	traza.save()
			# guardando los datos 
			#form.save()
			# y por ultimo redireccionando a la lista de paquetes
		#	return HttpResponseRedirect(self.get_success_url())
		#else:
			
		return HttpResponse("listar_todo")

class Historiallistar(ListView):
    model = Historial
    template_name = "listar_todo.html"