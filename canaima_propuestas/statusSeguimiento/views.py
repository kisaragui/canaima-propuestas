from django.shortcuts import render
from statusSeguimiento.models import Historial, PreEvaluador, ObsEvaluador
from postulacion.models import Package
from django.views.generic import CreateView, ListView, UpdateView, DetailView, FormView, TemplateView
from django.views.generic.edit import ProcessFormView, FormMixin
from django.core.urlresolvers import reverse_lazy
from statusSeguimiento.forms import HistorialForm, PreEvaluadorForm, ObsEvaluadorForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
# Create your views here.

class HistorialList(ListView, ProcessFormView, FormMixin):

	# lista los paquetes
	template_name="listar_status.html"
	model = Historial
	form_class = HistorialForm
	success_url = reverse_lazy("listar_status")	

	def post(self, request):
		#almacenando en variables los datos enviandos por via POST
		form = HistorialForm(request.POST)
		# se valida los datos via POST
		if form.is_valid():
			# almacenando en los variables sencillas los datos enviados via POST
			s = form.cleaned_data['status']
			n = form.cleaned_data["name_package"]
			# se hace un filtro en un query con los datos anteriores y pregunta si existe en la base de datos
			if self.model.objects.filter(name_package= n, status = s).exists():
				# envia un mensaje de error
				messages.add_message(request, messages.ERROR, 'Esta opcion ya existe.')
			else:
				# de lo contrario guarda el formulario
				form.save()

			return HttpResponseRedirect(self.get_success_url())
		else:

			return HttpResponseRedirect("listar_todo")
		

class Historiallistar(ListView):
 
	model = Historial
	template_name = "listar_todo.html"


class Principal(TemplateView):
    template_name = "index.html"


class PreguntasEvaluacion(UpdateView):
	model =PreEvaluador
	segundo_model = ObsEvaluador
	form_class = PreEvaluadorForm
	template_name = "formulario_evaluacion1.html"
	success_url = reverse_lazy("inicio")
	segundo_form_class = ObsEvaluadorForm

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