# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from postulacion.models import Package
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.views.generic.edit import ProcessFormView, FormMixin
from django.core.urlresolvers import reverse_lazy
from statusSeguimiento.models import Historial
from postulacion.forms import PackageForm, UpdateForm
from statusSeguimiento.forms import HistorialForm
from django.http import HttpResponseRedirect, HttpResponse
from evaluacion.models import CamposEvaluacion
from evaluacion.forms import EvaluacionForm, PackageNoEditableForm

class ListaEvaluacion(CreateView):

	model = CamposEvaluacion
	segundo_model= Package
	form_class = EvaluacionForm
	segundo_form_class = PackageNoEditableForm
	success_url = reverse_lazy("lista_evaluacion")
	template_name="lista_evaluacion2.html"

	def get_context_data(self, **kwargs):
		context = super(ListaEvaluacion, self).get_context_data(**kwargs)
		context["form2"] = self.segundo_form_class(self.request.GET)
		# en caso de que el formulario no tenga contexto lo genere vacio, para ingresar los datos
		if "form" not in context:
			# hace el pedido de los datos
 			context["form"] = self.form_class(self.request.GET)
		return context

# Create your views here.

# class ListaEvaluacion(ListView, ProcessFormView, FormMixin):
# 	# lista los paquetes y muestra el formulario de evaluacion 

# 	template_name="lista_evaluacion.html"
# 	model = Package
# 	segundo_model=PreEvaluador
# 	form_class = PreEvaluadorForm
# 	tercer_model=ObsEvaluador
# 	segundo_form_class = ObsEvaluadorForm
# 	success_url = reverse_lazy("lista_evaluacion")
	
# 	# enviando respuesta de la pedicion para actualizar el paquete

# 	def get_context_data(self, *args, **kwargs):
# 		context = super(ListaEvaluacion, self).get_context_data(**kwargs)
# 		# se llaman los modelos para ser visualizados por los nombres de los paquetes
# 		obs_list= self.tercer_model.objects.all().order_by("name")
# 		pre_list= self.segundo_model.objects.all().order_by("name")
# 		pack_list = self.model.objects.all().order_by("name_package")
# 		# se une los modelos en la tupla de 3 elementos para visualizar mejor
# 		listas=zip(pre_list, obs_list, pack_list)
# 		# se pasan  la variable al template por el comtexto
# 		if "listas" not in context:
# 			context["listas"] = listas
# 		return context

# 	def post(self, request, *args, **kwargs):
		
# 		# capturando la ID del paquete
# 		pk = request.POST["id"]
# 		#obteniendo la evaluacion  y las observaciones por la ID del paquete
# 		evaluacion = self.segundo_model.objects.get(id = pk)
# 		observacion = self.tercer_model.objects.get(id = pk)
# 		# cargando los datos intanciados 
# 		form = self.form_class(request.POST, instance= evaluacion)
# 		form2 = self.segundo_form_class(self.request.POST, instance=  observacion)
# 		# se valida los datos
# 		if form.is_valid() and form2.is_valid():
# 			form.save()
# 			form2.save()
# 			return HttpResponseRedirect(self.get_success_url())
# 		else:
# 			return HttpResponseRedirect(self.get_success_url())	


