from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('postulacion.urls')),
    url(r'^', include('statusSeguimiento.urls')),
    url(r'^', include('api.urls')),    
    url(r'^captcha/', include('captcha.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),

]

 