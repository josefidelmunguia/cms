#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from PIL import Image
from .models import Slider

class sliderForm(ModelForm):
    class Meta:
        model = Slider
        fields = ('usuario','nombre','categoria','imagen','fecha_inicio','fecha_fin')