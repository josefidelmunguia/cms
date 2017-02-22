from django.conf.urls import url,include
from productos.views import agregar_producto,agregar_etiqueta,agregar_categoria

urlpatterns = [
    url(r'^$', agregar_producto, name="agregar-producto"),
    url(r'^agregar_etiqueta$', agregar_etiqueta, name="agregar-etiqueta"),
    url(r'^agregar_categoria$', agregar_categoria, name="agregar-categoria"),
]