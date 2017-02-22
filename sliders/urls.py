from django.conf.urls import url,include
from sliders.views import agregar_slider,agregar_cat_slider

urlpatterns = [
    url(r'^$', agregar_slider, name="agregar-slider"),
    url(r'^agregar_categoria$', agregar_cat_slider, name="agregar-categoria"),
]
