from django.conf.urls import url,include
from enlaces.views import agregar_menu,agregar_enlace,menu_enlaces

urlpatterns = [
	url(r'^$', menu_enlaces, name="menu-enlaces"),
    url(r'^agregar_menu$', agregar_menu, name="agregar-menu"),
    url(r'^agregar_enlace$', agregar_enlace, name="agregar-enlace"),
    
]