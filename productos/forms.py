#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from PIL import Image
from .models import Producto

class productoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('usuario','nombre','categoria','etiqueta','sku','stock','imagen','fecha_publicacion')