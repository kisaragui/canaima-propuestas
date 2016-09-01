from django.contrib.auth.models import User
from rest_framework import serializers
from postulacion.models import Package, Package_status

class PackageSerializer(serializers.ModelSerializer):
    
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Package
        fields = ('id', 'repository', 'name_package', 'description_package', 'email') #, 'owner')

class PackageStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Package_status
        fields = ('package_id', 'status')


class UserSerializer(serializers.ModelSerializer):
    
    packages = serializers.PrimaryKeyRelatedField(many=True, queryset=Package.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'packages')
