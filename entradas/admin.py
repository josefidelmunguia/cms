from django.contrib import admin
from entradas.models import Categoria_Entrada,Comentario_Entrada,Etiqueta_Entrada,Entrada

@admin.register(Categoria_Entrada)
class Categoria_EntradaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Comentario_Entrada)
class Comentario_EntradaAdmin(admin.ModelAdmin):
	list_display = ('id','usuario','nombre','comentario')

@admin.register(Etiqueta_Entrada)
class Etiqueta_EntradaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
	list_display = ('id','usuario','titulo','categoria','etiqueta','comentario','fecha_creacion','fecha_publicacion')