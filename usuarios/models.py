from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	nombre = models.CharField(max_length=35)
	
	def __unicode__(self):
		return unicode(self.nombre)

class Usuario(models.Model):
	usuario = models.OneToOneField(User)
	perfil = models.ForeignKey(Perfil)
	entradas_usuario = models.PositiveIntegerField()

	def __unicode__(self):
		return unicode(self.usuario)