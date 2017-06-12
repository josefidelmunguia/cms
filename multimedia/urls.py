from django.conf.urls import url,include
from multimedia.views import menu_multimedia,agregar_multimedia

urlpatterns = [
    url(r'^$',menu_multimedia, name="menu-multimedia"),
    url(r'^agregar_multimedia$',agregar_multimedia, name="agregar-multimedia"),
]