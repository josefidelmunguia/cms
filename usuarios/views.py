#encoding:utf-8
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import Usuario

def login(request):
    page_title = "Inicio de Sesión"
    user = request.user
    template ="login.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def registrar_usuario(request):
    page_title = "Registrar usuario"
    user = request.user
    template ="registrar_usuario.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def menu_usuarios(request):
    page_title = "Menú usuarios"
    user = request.user
    usuario = Usuario.objects.all()
    template ="menu_usuarios.html" 
    return render(request,template, locals())