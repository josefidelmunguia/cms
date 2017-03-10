from __future__ import unicode_literals
from django.db import models
from paginas.models import Pagina
from entradas.models import Categoria_Entrada
from productos.models import Categoria_Producto

class Menu(models.Model):
	nombre = models.CharField(max_length=35)

	def __unicode__(self):
		return unicode(self.nombre)

class Enlace(models.Model):
	titulo = models.CharField(max_length=35)
	enlace_personalizado = models.CharField(max_length=35)
	categoria_producto = models.ForeignKey(Categoria_Producto)
	categoria_entrada = models.ForeignKey(Categoria_Entrada)
	menu = models.ForeignKey(Menu)
	pagina = models.ForeignKey(Pagina)
	
	def __unicode__(self):
		return unicode(self.titulo)