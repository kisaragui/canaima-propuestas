from django.conf.urls import url, include
from evaluacion.views import ListaEvaluacion

urlpatterns = [
    url(r'^evaluacion/$', ListaEvaluacion.as_view(), name= "lista_evaluacion"),
]	