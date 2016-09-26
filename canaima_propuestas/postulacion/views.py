from postulacion.models import Package
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from statusSeguimiento.models import Historial
from postulacion.forms import PackageForm
from statusSeguimiento.forms import HistorialForm
from django.http import HttpResponseRedirect

class PackageList(ListView):

	template_name="listar.html"
	model = Package

class PackageCreate(CreateView):
	
	template_name="postulacion.html"
	model = Package
	form_class = PackageForm
	success_url = reverse_lazy("listar")	
	segundo_form_class = HistorialForm

	def get_context_data(self, **kwargs):
		context = super(PackageCreate, self).get_context_data(**kwargs)
		if "form" not in context:
			context["form"] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(self.request.POST)		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(self.get_success_url("listar"))
		else:
		 	return self.render_to_response(self.get_context_data(form=form))

		#datos2.id_name_package = datos1.id_name_package
		#datos2.save()


	#context_object_name = "paquetes"
	


	# def get(self, request, format=None):
	# 	package = Package.objects.all()
	# 	serializer = PackageSerializer(Package, many=True)
	# 	return Response(serializer.data)

	# def post(self, request, format=None):
	# 	package = Package.objects.all()
	# 	serializer = PackageSerializer(Package, data=request.data)
	# 	if serializer.is_valid(): 
	# 		serializer.save()
	# 	 	return Response(serializer.data)
	

	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	#Packages = Package.objects.all()
	#serializer_class = PackageSerializer
	


   	#def perform_create(self, serializer):
	#		serializer.save(owner=self.request.user)

# Vista que permite actualizar y eliminar una postulacion
# class PackageDetail(generics.RetrieveUpdateDestroyAPIView):

# 	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                       IsOwnerOrReadOnly,)
# 	queryset = Package.objects.all()
# 	serializer_class = PackageSerializer

# class PaquetesEnDetalle(generics.ListUpdateAPIView):
	
# queryset = Package.objects.all()
# serializer_class = PackageSerializer

# Vista que permite listar y crear los status postulaciones
# class PackageStatusList(generics.ListCreateAPIView):

#	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# 	queryset = Package_status.objects.all()
#	serializer_class = PackageStatusSerializer

# Vista que permite actualizar status de una postulacion
# class PackageStatusDetail(generics.RetrieveUpdateDestroyAPIView):
# 
# 	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                       IsOwnerOrReadOnly,)
# queryset = Package_status.objects.all()
# 	serializer_class = PackageStatusSerializer

# class UserList(generics.ListAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

