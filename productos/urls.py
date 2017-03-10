from django.conf.urls import url,include
from productos.views import agregar_producto,agregar_etiqueta,agregar_categoria,menu_productos

urlpatterns = [
	url(r'^$', menu_productos, name="menu-productos"),
	url(r'^agregar_etiqueta$', agregar_etiqueta, name="agregar-etiqueta"),
    url(r'^agregar_producto$', agregar_producto, name="agregar-producto"),
    url(r'^agregar_categoria$', agregar_categoria, name="agregar-categoria"),  
]