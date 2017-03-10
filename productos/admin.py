from django.contrib import admin
from productos.models import Categoria_Producto,Etiqueta_Producto,Producto

@admin.register(Etiqueta_Producto)
class Etiqueta_ProductoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Categoria_Producto)
class Categor_ProductoiaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	list_display = ('id','usuario','nombre','categoria','etiqueta','sku','stock','precio','slugs','fecha_creacion','fecha_publicacion')

	prepopulated_fields = {'slugs' : ('nombre',)} 