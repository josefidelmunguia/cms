#encoding:utf-8
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import Menu,Pagina,Categoria_Producto,Categoria_Entrada

@login_required(login_url='/usuarios/login/')
def agregar_menu(request):
    page_title = "Agregar Menu"
    user = request.user
    template ="agregar_menu.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_enlace(request):
    page_title = "Agregar Enlace"
    user = request.user
    pagina = Pagina.objects.all()
    categoria_producto = Categoria_Producto.objects.all()
    categoria_entrada = Categoria_Entrada.objects.all()
    menu = Menu.objects.all()
    template ="agregar_enlace.html" 
    return render(request,template, locals())