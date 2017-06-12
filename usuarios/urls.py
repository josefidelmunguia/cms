from django.conf.urls import url,include
from usuarios.views import registrar_usuario,login,menu_usuarios,completar_informacion

urlpatterns = [
	url(r'^$', menu_usuarios, name="menu-usuarios"),
	url(r'^login/$', login, name="login"),
    url(r'^registrar$', registrar_usuario, name="registro-usuario"),
    url(r'^completar$', completar_informacion, name="completar-info"),
]