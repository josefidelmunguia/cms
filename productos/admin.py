from django.contrib import admin
from productos.models import Categoria_Producto
from productos.models import Etiqueta_Producto
from productos.models import Producto

@admin.register(Etiqueta_Producto)
class Etiqueta_ProductoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Categoria_Producto)
class Categor_ProductoiaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	list_display = ('id','usuario','nombre','sku','stock','precio','categoria','etiqueta','fecha_creacion','fecha_publicacion')