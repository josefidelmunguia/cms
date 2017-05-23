#encoding:utf-8
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import Categoria,Slider

@login_required(login_url='/usuarios/login/')
def agregar_slider(request):
    page_title = "AGREGAR SLIDER"
    user = request.user
    categoria = Categoria.objects.all()
    template ="agregar_slider.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_cat_slider(request):
    page_title = "AGREGAR CATEGORIA"
    user = request.user
    template ="agregar_cat_slider.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def menu_sliders(request):
    page_title = "SLIDERS"
    user = request.user
    slider = Slider.objects.all()
    template ="menu_sliders.html" 
    return render(request,template, locals())

