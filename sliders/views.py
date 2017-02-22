#encoding:utf-8
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import Categoria

@login_required(login_url='/usuarios/login/')
def agregar_slider(request):
    page_title = "Agregar Slider"
    user = request.user
    categoria = Categoria.objects.all()
    template ="agregar_slider.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_cat_slider(request):
    page_title = "Agregar Categoria"
    user = request.user
    template ="agregar_cat_slider.html" 
    return render(request,template, locals())
