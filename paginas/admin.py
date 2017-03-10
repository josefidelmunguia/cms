from django.contrib import admin
from paginas.models import Pagina

@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
	list_display = ('id','usuario','titulo','contenido','slugs','fecha_creacion','fecha_publicacion')

	prepopulated_fields = {'slugs' : ('titulo',)} 