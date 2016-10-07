from postulacion.models import Package
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.core.urlresolvers import reverse_lazy
from statusSeguimiento.models import Historial
from postulacion.forms import PackageForm
from statusSeguimiento.forms import HistorialForm
from django.http import HttpResponseRedirect

class PackageDetail(DetailView):

	# muestra los datos completos de los paquetes
	model = Package
	template_name = "detalle.html"	

class PackageList(ListView):

	# lista los paquetes
	template_name="listar.html"
	model = Package

class PackageCreate(CreateView):
	
	# crear los paquetes
	template_name="postulacion.html"
	model = Package
	form_class = PackageForm
	success_url = reverse_lazy("listar")	
	segundo_form_class = HistorialForm

	# primero se crea el contexto del formulario
	def get_context_data(self, **kwargs):
		context = super(PackageCreate, self).get_context_data(**kwargs)
		# en caso de que el formulario no tenga contexto lo genere vacio, para ingresar los datos
		if "form" not in context:
			# hace el pedido de los datos
			context["form"] = self.form_class(self.request.GET)
		return context

	# envia las respuesta 
	def post(self, request, *args, **kwargs):
		# para que reciba el ojteto
		self.object = self.get_object
		# se carga la respuesta
		form = self.form_class(self.request.POST)
		# se validan los datos
		if form.is_valid():
			form.save()
			# se redirige al sitio que tiene de nombre la variable "success_url" cuando el guardado sea un exito
			return HttpResponseRedirect(self.get_success_url())
		else:
			# de lo contrario, devuelve el formulario
		 	return self.render_to_response(self.get_context_data(form=form))

# actualiza los paquetes 
class PackageUpdate(UpdateView):

	model= Package
	template_name= "editar.html"
	form_class = PackageForm
	success_url = reverse_lazy("listar")

	# primero se genere el contexto del formulario
	def get_context_data(self, **kwargs):
		# se carga el contexto
		context = super(PackageUpdate, self).get_context_data(**kwargs)
		# se crea un variable que contenga que capture la ID de los paquetes
		pk = self.kwargs.get("pk", 0)
		# se captura o extrae el paquete por ID
		paquete = self.model.objects.get(id=pk)
		if "form" not in context:
			# se muestra el contexto del formulario del paquete a actualizar
			context ["form"] =self.form_class()
		context["id"] = pk
		return context
	
	# enviando respuesta de la pedicion para actualizar el paquete	
	def post(self, request, *args, **kwargs):
		# obteniendo objeto del paquete
		self.object = self.get_object
		# capturando la ID del paquete
		id_paquete = kwargs["pk"]
		#obteniendo el paquete por la ID 
		paquete = self.model.objects.get(id = id_paquete)
		# cargando los datos intanciados 
		form = self.form_class(request.POST, instance= paquete)
		# validando los datos a actualizar
		if form.is_valid():
			# guardando los datos 
			form.save()
			# y por ultimo redireccionando a la lista de paquetes
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())	





