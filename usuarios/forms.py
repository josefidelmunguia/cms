#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from PIL import Image
from .models import Usuario

class registerForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password',)

class comp1Form(ModelForm):
	class Meta:
		model =  User
		fields =('first_name','last_name')

class comp2Form(ModelForm):
	class Meta:
		model =  Usuario
		fields =('perfil','entradas_usuario')



		