#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from PIL import Image
from .models import Multimedia

class multimediaForm(ModelForm):
    class Meta:
        model = Multimedia
        fields = ('usuario','titulo','tipo','leyenda','texto_alternativo','archivo','fecha_publicacion')
