from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import renderers
from statusSeguimiento.models import Historial
from statusSeguimiento.serializers import HistorialSerializer
from postulacion.models import Package
from postulacion.serializers import PackageSerializer
# Create your views here.


class HistorialList(generics.ListAPIView):

	queryset = Package.objects.all()
	serializer_class = PackageSerializer

	#queryset = Historial.objects.all()
	#serializer_class = HistorialSerializer
