from django.contrib import admin
from sliders.models import Categoria,Slider

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
	list_display = ('id','usuario','nombre','categoria','imagen','fecha_creacion','fecha_inicio','fecha_fin')