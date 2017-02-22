from django.conf.urls import url,include
from paginas.views import index,agregar_pagina

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^agregar_pagina$', agregar_pagina, name="agregar-pagina"),
]