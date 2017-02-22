from __future__ import unicode_literals
from django.db import models
from usuarios.models import Usuario

class Categoria_Entrada(models.Model):
	nombre = models.CharField(max_length=25)
	imagen =models.ImageField(upload_to='img/entradas',)
	
	def __unicode__(self):
		return unicode(self.nombre)

class Comentario_Entrada(models.Model):
	usuario = models.ForeignKey(Usuario,blank=True,null=True)
	nombre = models.CharField(max_length=35)
	comentario = models.CharField(max_length=70)

	def __unicode__(self):
		return unicode(self.nombre)

class Etiqueta_Entrada(models.Model):
	nombre = models.CharField(max_length=25)

	def __unicode__(self):
		return unicode(self.nombre)

class Entrada(models.Model):
	usuario = models.ForeignKey(Usuario)
	titulo = models.CharField(max_length=45)
	categoria = models.ForeignKey(Categoria_Entrada)
	etiqueta = models.ForeignKey(Etiqueta_Entrada)
	comentario = models.ForeignKey(Comentario_Entrada)
	imagen = models.ImageField(upload_to='img/entradas',)
	fecha_creacion = models.DateField(auto_now_add=True)
	fecha_publicacion = models.DateField()

	def __unicode__(self):
		return unicode(self.titulo)