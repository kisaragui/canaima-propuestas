from django.conf.urls import url, include
from postulacion.views import PackageList

urlpatterns = [
    url(r'^postulacion/$', PackageList.as_view(), name= "crear"),
    #url(r'^postulacion/(?P<pk>[0-9]+)/$', views.PackageDetail.as_view()),
    #url(r'^postulacion/status/$', views.PackageStatusList.as_view()),
    #url(r'^postulacion/status/(?P<pk>[0-9]+)/$', views.PackageStatusDetail.as_view()),
    #url(r'^users/$', views.UserList.as_view()),
	#url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]