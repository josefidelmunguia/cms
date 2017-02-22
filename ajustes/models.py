from __future__ import unicode_literals
from django.db import models

class Ajuste(models.Model):
	titulo_sitio = models.CharField(max_length=40)
	descripcion_corta = models.CharField(max_length=60)

	def __unicode__(self):
		return unicode(self.titulo_sitio)