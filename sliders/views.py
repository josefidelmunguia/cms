#encoding:utf-8
from django.template.context_processors import csrf
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import Categoria,Slider
from django.template.context import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario
from .forms import sliderForm

@login_required(login_url='/usuarios/login/')
def agregar_slider(request):
    user = request.user
    usuario = Usuario.objects.get(usuario=user)
    slider = Slider.objects.all()
    categoria = Categoria.objects.all()
    if request.method == 'POST':
        form_slider = sliderForm(request.POST,request.FILES)
        if form_slider.is_valid():
            slider = form_slider.save(commit=False)
            slider.save()
            return redirect('menu-sliders')
    else:
        form_slider = sliderForm()
    args = {}
    args.update(csrf(request))
    page_title = "AGREGAR SLIDER"
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

