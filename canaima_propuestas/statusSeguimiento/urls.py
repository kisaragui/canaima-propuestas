from django.conf.urls import url, include
from statusSeguimiento import views
from statusSeguimiento.views import HistorialList, Historiallistar

urlpatterns = [

	url(r'^seguimiento/$', HistorialList.as_view(), name="listar_status"),
	url(r'^seguimiento/listar/$', Historiallistar.as_view(), name="listar_todo"),
]