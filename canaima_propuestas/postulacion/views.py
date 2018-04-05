from postulacion.models import Package
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.views.generic.edit import ProcessFormView, FormMixin
from django.core.urlresolvers import reverse_lazy
from statusSeguimiento.models import Historial, PreEvaluador, ObsEvaluador
from postulacion.forms import PackageForm, UpdateForm
from statusSeguimiento.forms import HistorialForm, PreEvaluadorForm, ObsEvaluadorForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

class PackageCreate(CreateView):
	# crear los paquetes
	
	template_name="postulacion.html"
	model = Package
	segundo_model = User
	form_class = PackageForm
	#segundo_form_class = CaptchaForm
	success_url = reverse_lazy("lista")	
	
	# primero se crea el contexto del formulario
	def get_context_data(self, **kwargs):
		context = super(PackageCreate, self).get_context_data(**kwargs)
		# en caso de que el formulario no tenga contexto lo genere vacio, para ingresar los datos
		if "form" not in context:
			# hace el pedido de los datos
 			context["form"] = self.form_class(self.request.GET)
 		#if "captcha" not in context:
 		#	context["captcha"] = self.segundo_form_class(self.request.GET)
		return context

	# envia las respuesta 
	def post(self, request, *args, **kwargs):
		# para que reciba el ojteto
		self.object = self.get_object
		u = request.user
		registro = self.segundo_model.objects.get(username=u)
		# se carga la respuesta en el formulario
		form = self.form_class(self.request.POST)
		# se validan los datos
		if form.is_valid():
			nuevoForm = form.save(commit=False)
			nuevoForm.usuario = registro.username
			nuevoForm.email = registro.email
			nuevoForm.save()
			# se redirige al sitio que tiene de nombre la variable "success_url" cuando el guardado sea un exito
			return HttpResponseRedirect(self.get_success_url())
		else:
			# de lo contrario, devuelve el formulario
		 	return self.render_to_response(self.get_context_data(form=form))


class PackageDetail(DetailView):
	# muestra un paquete detallado 
	
	model = Package
	template_name = "detalle.html"	
	
	def get_context_data(self, *args, **kwargs):

		pk = self.kwargs["pk"]
		record = self.model.objects.get(id=pk)
		context = super(PackageDetail, self).get_context_data(**kwargs)
		detallado = Historial.objects.filter(name_package=record.name_package)
		context['detalle_list'] = detallado
		return context

class PackageLista(ListView):
	# lista los paquetes

	template_name="lista.html"
	model = Package

	def get_context_data(self, *args, **kwargs):
		context = super(PackageLista, self).get_context_data(**kwargs)
		# en caso de que el formulario no tenga contexto lo genere vacio, para ingresar los datos
		if "listado_list" not in context:
			context["listado_list"] = self.model.objects.all().order_by("name_package")
		return context
		
class ListaEvaluacion(ListView, ProcessFormView, FormMixin):
	# lista los paquetes y muestra el formulario de evaluacion 

	template_name="lista_evaluacion.html"
	model = Package
	segundo_model=PreEvaluador
	form_class = PreEvaluadorForm
	tercer_model=ObsEvaluador
	segundo_form_class = ObsEvaluadorForm
	success_url = reverse_lazy("lista_evaluacion")
	
	# enviando respuesta de la pedicion para actualizar el paquete

	def get_context_data(self, *args, **kwargs):
		context = super(ListaEvaluacion, self).get_context_data(**kwargs)
		# se llaman los modelos para ser visualizados por los nombres de los paquetes
		obs_list= self.tercer_model.objects.all().order_by("name")
		pre_list= self.segundo_model.objects.all().order_by("name")
		pack_list = self.model.objects.all().order_by("name_package")
		# se une los modelos en la tupla de 3 elementos para visualizar mejor
		listas=zip(pre_list, obs_list, pack_list)
		# se pasan  la variable al template por el comtexto
		if "listas" not in context:
			context["listas"] = listas
		return context

	def post(self, request, *args, **kwargs):
		
		# capturando la ID del paquete
		pk = request.POST["id"]
		#obteniendo la evaluacion  y las observaciones por la ID del paquete
		evaluacion = self.segundo_model.objects.get(id = pk)
		observacion = self.tercer_model.objects.get(id = pk)
		# cargando los datos intanciados 
		form = self.form_class(request.POST, instance= evaluacion)
		form2 = self.segundo_form_class(self.request.POST, instance=  observacion)
		# se valida los datos
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())	


# actualiza los paquetes 
# class PackageUpdate(UpdateView):

# 	model= Package
# 	template_name= "editar.html"
# 	form_class = PackageForm
# 	success_url = reverse_lazy("lista")

# 	# primero se genere el contexto del formulario
# 	def get_context_data(self, **kwargs):
# 		# se carga el contexto
# 		context = super(PackageUpdate, self).get_context_data(**kwargs)
# 		# se crea un variable que contenga que capture la ID de los paquetes
# 		pk = self.kwargs.get("pk", 0)
# 		# se captura o extrae el paquete por ID
# 		paquete = self.model.objects.get(id=pk)
# 		if "form" not in context:
# 			# se muestra el contexto del formulario del paquete a actualizar
# 			context ["form"] =self.form_class()
# 		context["id"] = pk
# 		return context
	
# 	# enviando respuesta de la pedicion para actualizar el paquete	
# 	def post(self, request, *args, **kwargs):
# 		# obteniendo objeto del paquete
# 		self.object = self.get_object
# 		# capturando la ID del paquete
# 		id_paquete = kwargs["pk"]
# 		#obteniendo el paquete por la ID 
# 		paquete = self.model.objects.get(id = id_paquete)
# 		# cargando los datos intanciados 
# 		form = self.form_class(request.POST, instance= paquete)
# 		# validando los datos a actualizar
# 		if form.is_valid():
# 			# guardando los datos 
# 			form.save()
# 			# y por ultimo redireccionando a la lista de paquetes
# 			return HttpResponseRedirect(self.get_success_url())
# 		else:
# 			return HttpResponseRedirect(self.get_success_url())	


class PackageStatusUpdate(ListView, ProcessFormView, FormMixin):

	# lista los paquetes
	template_name="lista_status_update.html"
	model = Package
	form_class = UpdateForm
	
	def post(self, request):
		
		# capturando la ID del paquete
		id_paquete = self.request.POST["id"]
		# pasando la obteniendo el paquete por la ID 
		paquete = self.model.objects.get(id = id_paquete)
		# almacenando en variables los datos enviandos por via POST y por la instancia
		form = self.form_class(request.POST, instance= paquete)
		# se valida los datos via POST
		if form.is_valid():
			# almacenando en los variables sencillas los datos enviados via POST
			s = form.cleaned_data['status']
			n = form.cleaned_data["name_package"]
			# se hace un filtro en un query con los datos anteriores y pregunta si existe en la base de datos
			if Historial.objects.filter(name_package= n, status = s).exists():
				# envia un mensaje de error
				messages.add_message(request, messages.ERROR, 'Esta opcion ya existe.')
			else:
				# de lo contrario guarda el formulario
				form.save()
				return HttpResponseRedirect(reverse_lazy("lista_todo"))


			return HttpResponseRedirect(reverse_lazy("lista_status_update"))
			
		else:

			return HttpResponseRedirect(reverse_lazy("lista_todo"))


