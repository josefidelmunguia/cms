#encoding:utf-8
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required

def index(request):
    page_title = "Bienvenido"
    user = request.user
    template ="index.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_pagina(request):
    page_title = "Agregar Página"
    user = request.user
    template ="agregar_pagina.html" 
    return render(request,template, locals())