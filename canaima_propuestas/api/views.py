from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from postulacion.models import Package
from api.serializers import PackageSerializer
from rest_framework.views import APIView

class PackageListJSON(APIView):

	def get(self, request, format=None):
		package = Package.objects.all()
		serializer = PackageSerializer(package, many=True)
	 	return Response (serializer.data) 