from django.conf.urls import url, include
from statusSeguimiento import views
from statusSeguimiento.views import HistorialList, HistorialEnDetalle

urlpatterns = [

	url(r'^seguimiento/$', HistorialList.as_view(), name="listar_status"),
	url(r'^postulacion/(?P<pk>\d+)$', HistorialEnDetalle.as_view(), name = "detalle"),

]