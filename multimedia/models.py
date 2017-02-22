from __future__ import unicode_literals
from django.db import models
from usuarios.models import Usuario

class Multimedia(models.Model):
	usuario = models.ForeignKey(Usuario)
	titulo = models.CharField(max_length=30)
	tipo = models.CharField(max_length=10)
	leyenda = models.CharField(max_length=50)
	texto_alternatico = models.CharField(max_length=40)
	archivo = models.FileField(upload_to='arch/multimedia',)
	fecha_creacion = models.DateField(auto_now_add=True)
	fecha_publicacion = models.DateField()

	def __unicode__(self):
		return unicode(self.titulo)
