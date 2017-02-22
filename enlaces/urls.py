from django.conf.urls import url,include
from enlaces.views import agregar_menu,agregar_enlace

urlpatterns = [
    url(r'^agregar_menu$', agregar_menu, name="agregar-menu"),
    url(r'^$', agregar_enlace, name="agregar-enlace"),
]