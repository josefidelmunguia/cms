from django.contrib import admin
from usuarios.models import Perfil,Usuario

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('id','usuario','perfil','entradas_usuario')