#encoding:utf-8
from django.template.context_processors import csrf
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import auth
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Categoria_Producto,Etiqueta_Producto,Producto
from .models import Usuario
from .forms import productoForm

@login_required(login_url='/usuarios/login/')
def agregar_producto(request):
    user = request.user
    usuario = Usuario.objects.get(usuario=user)
    categoria_producto = Categoria_Producto.objects.all()
    etiqueta_producto = Etiqueta_Producto.objects.all()
    producto = Producto.objects.all()
    if request.method == 'POST':
        form_producto = productoForm(request.POST,request.FILES)
        if form_producto.is_valid():
            producto = form_producto.save(commit=False)
            producto.save()
            return redirect('menu-productos')
    else:
        form_producto = productoForm()
    args = {}
    args.update(csrf(request))
    page_title = "AGREGAR PRODUCTO"
    template ="agregar_producto.html"
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_etiqueta(request):
    page_title = "AGREGAR ETIQUETA"
    user = request.user
    template ="agregar_eti_producto.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_categoria(request):
    page_title = "AGREGAR CATEGORIA"
    user = request.user
    template ="agregar_cat_producto.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def menu_productos(request):
    page_title = "PRODUCTOS"
    user = request.user
    producto = Producto.objects.all()
    template ="menu_productos.html" 
    return render(request,template, locals())