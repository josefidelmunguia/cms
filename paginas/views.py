#encoding:utf-8
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import Pagina
from usuarios.models import Usuario

@login_required(login_url='/usuarios/login/')
def index(request):
    page_title = "BIENVENIDOS...!"
    user = request.user
    usuario = Usuario.objects.get(usuario=user)
    template ="index.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_pagina(request):
    page_title = "AGREGAR PÁGINA"
    user = request.user
    template ="agregar_pagina.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def menu_paginas(request):
    page_title = "PÁGINAS"
    user = request.user
    pagina = Pagina.objects.all()
    template ="menu_paginas.html" 
    return render(request,template, locals())


