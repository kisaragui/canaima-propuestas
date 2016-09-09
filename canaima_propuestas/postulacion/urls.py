from django.conf.urls import url, include
from postulacion import views

urlpatterns = [
    url(r'^postulacion/$', views.PackageList.as_view()),
    url(r'^postulacion/(?P<pk>[0-9]+)/$', views.PackageDetail.as_view()),
    #url(r'^postulacion/status/$', views.PackageStatusList.as_view()),
    #url(r'^postulacion/status/(?P<pk>[0-9]+)/$', views.PackageStatusDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]