from django.contrib import admin
from multimedia.models import Multimedia

@admin.register(Multimedia)
class MultimediaAdmin(admin.ModelAdmin):
	list_display = ('id','usuario','titulo','tipo','leyenda','texto_alternatico','fecha_creacion','fecha_publicacion')

