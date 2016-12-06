from django.conf.urls import url, include
from postulacion.views import PackageListAdmin, PackageList, PackageCreate, PackageUpdate, PackageDetail, PackageListUpdate

urlpatterns = [
    url(r'^postulacion/$', PackageCreate.as_view(), name= "crear"),
    url(r'^postulacion/listar$', PackageList.as_view(), name= "listar"),
    url(r'^postulacion/listar/evaluar/$', PackageListAdmin.as_view(), name= "listar_admin"),
    url(r'^postulacion/editar/(?P<pk>\d+)$', PackageUpdate.as_view(), name = "editar"),
    url(r'^postulacion/(?P<pk>\d+)$', PackageDetail.as_view(), name = "detalle"),
    url(r'^postulacion/listar/status/$', PackageListUpdate.as_view(), name= "listar_status_update"),
    
]	