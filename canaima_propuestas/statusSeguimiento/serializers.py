from rest_framework import serializers
from postulacion.models import Package
from statusSeguimiento.models import Historial

class HistorialSerializer(serializers.ModelSerializer):
    

	class Meta:
		model = Historial
		fields = ('id', "fecha_actualizada", 'status') 