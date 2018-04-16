from django.conf.urls import url, include
from postulacion.views import PackageLista, PackageCreate, PackageDetail, PackageStatusUpdate

urlpatterns = [
    url(r'^postulacion/$', PackageCreate.as_view(), name= "crear"),
    url(r'^postulacion/lista$', PackageLista.as_view(), name= "lista"),
#    url(r'^postulacion/lista/evaluar/$', ListaEvaluacion.as_view(), name= "lista_evaluacion"),
    url(r'^postulacion/(?P<pk>\d+)$', PackageDetail.as_view(), name = "detalle"),
    url(r'^postulacion/lista/status/$', PackageStatusUpdate.as_view(), name= "lista_status_update"),
    
]	