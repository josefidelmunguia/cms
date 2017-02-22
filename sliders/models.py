from __future__ import unicode_literals
from django.db import models
from usuarios.models import Usuario

class Categoria(models.Model):
	nombre = models.CharField(max_length=25)

	def __unicode__(self):
		return unicode(self.nombre)

class Slider(models.Model):
	usuario = models.ForeignKey(Usuario)
	nombre = models.CharField(max_length=40)
	categoria = models.ForeignKey(Categoria)
	imagen =models.ImageField(upload_to='img/sliders',)
	fecha_creacion = models.DateField(auto_now_add=True)
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()

	def __unicode__(self):
		return unicode(self.nombre)
