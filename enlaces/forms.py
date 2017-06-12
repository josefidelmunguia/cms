#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from PIL import Image
from .models import Enlace

class enlaceForm(ModelForm):
    class Meta:
        model = Enlace
        fields = ('titulo','enlace_personalizado','pagina','categoria_producto','categoria_entrada','menu')
