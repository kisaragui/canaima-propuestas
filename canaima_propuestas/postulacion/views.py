from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import renderers
from postulacion.serializers import UserSerializer
from postulacion.permissions import IsOwnerOrReadOnly
from postulacion.models import Package
from postulacion.serializers import PackageSerializer
from statusSeguimiento.models import Historial
from statusSeguimiento.serializers import HistorialSerializer
#Vista que permite listar y crear las postulaciones
class PackageList(ListCreateAPIView):

	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	lista = Package.objects.all()
	serializer_class = PackageSerializer
	
	lista2 = Historial.objects.all()
	serializar= HistorialSerializer


   	#def perform_create(self, serializer):
	#		serializer.save(owner=self.request.user)

#Vista que permite actualizar y eliminar una postulacion
class PackageDetail(generics.RetrieveUpdateDestroyAPIView):

	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                  IsOwnerOrReadOnly,)
	queryset = Package.objects.all()
	serializer_class = PackageSerializer

#class PaquetesEnDetalle(generics.ListUpdateAPIView):
	
#	queryset = Package.objects.all()
#	serializer_class = PackageSerializer

#Vista que permite listar y crear los status postulaciones
#class PackageStatusList(generics.ListCreateAPIView):

	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#	queryset = Package_status.objects.all()
#	serializer_class = PackageStatusSerializer

#Vista que permite actualizar status de una postulacion
#class PackageStatusDetail(generics.RetrieveUpdateDestroyAPIView):
#
#	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#    #                  IsOwnerOrReadOnly,)
#	queryset = Package_status.objects.all()
#	serializer_class = PackageStatusSerializer

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

