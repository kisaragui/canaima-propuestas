from rest_framework import serializers
from postulacion.models import Package

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ("id", "repository", "name_package", "description_package", "status", "email", "fecha")


