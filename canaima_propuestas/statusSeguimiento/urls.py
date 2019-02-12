from django.conf.urls import url, include
from statusSeguimiento import views
from statusSeguimiento.views import HistorialLista, Principal

urlpatterns = [


	url(r'^seguimiento/lista/$', HistorialLista.as_view(), name="lista_todo"),
	url(r'^$', Principal.as_view(), name="inicio"),
]