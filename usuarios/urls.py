from django.conf.urls import url,include
from usuarios.views import registrar_usuario,login

urlpatterns = [
    url(r'^registrar$', registrar_usuario, name="registro-usuario"),
    url(r'^login/$', login, name="login"),
]