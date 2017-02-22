from django.contrib import admin
from ajustes.models import Ajuste

@admin.register(Ajuste)
class AjusteAdmin(admin.ModelAdmin):
	list_display = ('id','titulo_sitio','descripcion_corta')