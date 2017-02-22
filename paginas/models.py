from __future__ import unicode_literals
from django.db import models
from usuarios.models import Usuario

class Pagina(models.Model):
	usuario = models.ForeignKey(Usuario)
	titulo = models.CharField(max_length=35)
	contenido = models.CharField(max_length=400)
	fecha_creacion = models.DateField(auto_now_add=True)
	fecha_publicacion = models.DateField()
	slugs = models.SlugField(max_length=50)

	def __unicode__(self):
		return unicode(self.titulo)