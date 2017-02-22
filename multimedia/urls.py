from django.conf.urls import url,include
from multimedia.views import agregar_multimedia

urlpatterns = [
    url(r'^$',agregar_multimedia, name="agregar-multimedia"),
]