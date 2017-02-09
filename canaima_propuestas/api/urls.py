from django.conf.urls import url, include
from api.views import PackageListJSON
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^API/$', PackageListJSON.as_view(), name= "list"),

]

urlpatterns = format_suffix_patterns(urlpatterns)