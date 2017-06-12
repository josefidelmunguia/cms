#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from PIL import Image
from .models import Entrada

class entradaForm(ModelForm):
    class Meta:
        model = Entrada
        fields = ('usuario','titulo','categoria','etiqueta','imagen','fecha_publicacion')