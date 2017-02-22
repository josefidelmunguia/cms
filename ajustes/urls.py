from django.conf.urls import url,include
from ajustes.views import ajustes

urlpatterns = [
    url(r'^$', ajustes, name="ajustes"),
]