from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include ('paginas.urls')),
    url(r'^usuarios/', include ('usuarios.urls')),
    url(r'^multimedia/', include ('multimedia.urls')),
    url(r'^sliders/', include ('sliders.urls')),
    url(r'^productos/', include ('productos.urls')),
    url(r'^entradas/', include('entradas.urls')),
    url(r'^enlaces/', include('enlaces.urls')),
    url(r'^ajustes/', include('ajustes.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)