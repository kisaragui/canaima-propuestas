from django.conf.urls import url, include
from statusSeguimiento import views

urlpatterns = [

	url(r'^seguimiento/$', views.HistorialList.as_view()),

]