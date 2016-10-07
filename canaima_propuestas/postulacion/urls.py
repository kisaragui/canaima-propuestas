from django.conf.urls import url, include
from postulacion.views import PackageList, PackageCreate, PackageUpdate, PackageDetail

urlpatterns = [
    url(r'^postulacion/$', PackageCreate.as_view(), name= "crear"),
    url(r'^postulacion/listar$', PackageList.as_view(), name= "listar"),
    url(r'^postulacion/editar/(?P<pk>\d+)$', PackageUpdate.as_view(), name = "editar"),
    url(r'^postulacion/(?P<pk>\d+)$', PackageDetail.as_view(), name = "detalle"),

]