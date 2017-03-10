from django.conf.urls import url,include
from entradas.views import agregar_entrada,agregar_etiqueta,agregar_categoria,agregar_comentario,menu_entradas

urlpatterns = [
	url(r'^$', menu_entradas, name="menu-entradas"),
    url(r'^agregar_entrada$', agregar_entrada, name="agregar-entrada"),
    url(r'^agregar_etiqueta$', agregar_etiqueta, name="agregar-etiqueta"),
    url(r'^agregar_categoria$', agregar_categoria, name="agregar-categoria"),
    url(r'^agregar_comentario$', agregar_comentario, name="agregar-comentario"),
]