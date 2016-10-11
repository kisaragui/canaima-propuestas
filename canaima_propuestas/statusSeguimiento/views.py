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

	def post(self, request):
		#almacenando en variables los datos enviandos por via POST
		s = request.POST["status"]
		n = request.POST["name_package"]
		form = HistorialForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())
		
		
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

class HistorialEnDetalle(ListView):

    
    template_name = "listar_todo.html"

    def get_context_data(self, request, **kwargs):
        # Call the base implementation first to get a context
        context = super(HistorialEnDetalle, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['detalle_list'] = Historial.objects.filter(name_package = kwargs["name_package"])
        return context