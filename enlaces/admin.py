from django.contrib import admin
from enlaces.models import Menu,Enlace

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Enlace)
class EnlanceAdmin(admin.ModelAdmin):
	list_display = ('id','titulo','enlace_personalizado','pagina','categoria_producto','categoria_producto','menu')