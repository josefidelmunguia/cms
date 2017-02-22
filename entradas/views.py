#encoding:utf-8
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import Categoria_Entrada,Comentario_Entrada,Etiqueta_Entrada

@login_required(login_url='/usuarios/login/')
def agregar_categoria(request):
    page_title = "Agregar Categoria"
    user = request.user
    template ="agregar_cat_entrada.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_etiqueta(request):
    page_title = "Agregar Etiqueta"
    user = request.user
    template ="agregar_eti_entrada.html" 
    return render(request,template, locals())

def agregar_comentario(request):
    page_title = "Agregar Comentario"
    user = request.user
    template ="agregar_com_entrada.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_entrada(request):
    page_title = "Agregar Entrada"
    user = request.user
    categoria_entrada = Categoria_Entrada.objects.all()
    etiqueta_entrada = Etiqueta_Entrada.objects.all()
    comentario_entrada = Comentario_Entrada.objects.all()
    template ="agregar_entrada.html" 
    return render(request,template, locals())