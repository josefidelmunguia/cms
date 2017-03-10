from django.conf.urls import url,include
from ajustes.views import ajustes,menu_ajustes

urlpatterns = [
    url(r'^$', menu_ajustes, name="menu-ajustes"),
    url(r'^agregar_ajuste$', ajustes, name="ajustes"),
]