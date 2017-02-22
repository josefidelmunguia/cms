from __future__ import unicode_literals
from django.db import models
from usuarios.models import Usuario

class Categoria_Producto(models.Model):
	nombre = models.CharField(max_length=25)
	imagen =models.ImageField(upload_to='img/productos',)
	
	def __unicode__(self):
		return unicode(self.nombre)

class Etiqueta_Producto(models.Model):
	nombre = models.CharField(max_length=25)

	def __unicode__(self):
		return unicode(self.nombre)

class Producto(models.Model):
	usuario = models.ForeignKey(Usuario)
	nombre = models.CharField(max_length=40)
	sku = models.CharField(max_length=20,unique=True)
	stock = models.CharField(max_length=20)
	precio = models.DecimalField(max_digits=7,decimal_places=2,blank=True,null=True)
	categoria = models.ForeignKey(Categoria_Producto)
	etiqueta = models.ForeignKey(Etiqueta_Producto)
	imagen = models.ImageField(upload_to='img/productos',)
	fecha_creacion = models.DateField(auto_now_add=True)
	fecha_publicacion = models.DateField()

	def __unicode__(self):
		return unicode(self.nombre)