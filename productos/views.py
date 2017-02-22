#encoding:utf-8
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import Categoria_Producto,Etiqueta_Producto

@login_required(login_url='/usuarios/login/')
def agregar_producto(request):
    page_title = "Agregar Producto"
    user = request.user
    categoria_producto = Categoria_Producto.objects.all()
    etiqueta_producto = Etiqueta_Producto.objects.all()
    template ="agregar_producto.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_etiqueta(request):
    page_title = "Agregar Etiqueta"
    user = request.user
    template ="agregar_eti_producto.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_categoria(request):
    page_title = "Agregar Categoria"
    user = request.user
    template ="agregar_cat_producto.html" 
    return render(request,template, locals())