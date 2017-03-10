from django.conf.urls import url,include
from paginas.views import index,agregar_pagina,menu_paginas

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^paginas$',menu_paginas, name="menu-paginas"),
    url(r'^agregar_pagina$', agregar_pagina, name="agregar-pagina"),
]