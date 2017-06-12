#encoding:utf-8
from django.template.context_processors import csrf
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario
from .models import Pagina
from .forms import paginaForm

@login_required(login_url='/usuarios/login/')
def index(request):
    page_title = "BIENVENIDOS...!"
    user = request.user
    usuario = Usuario.objects.get(usuario=user)
    template ="index.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_pagina(request):   
    user = request.user
    usuario = Usuario.objects.get(usuario=user)
    pagina = Pagina.objects.all()    
    if request.method == 'POST':
        form_pagina = paginaForm(request.POST)
        if form_pagina.is_valid():
            pagina = form_pagina.save(commit=False)
            pagina.save()
            return redirect('menu-paginas')
    else:
        form_pagina = paginaForm()
    args = {}
    args.update(csrf(request))
    page_title = "AGREGAR PÁGINA"
    template ="agregar_pagina.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def menu_paginas(request):
    page_title = "PÁGINAS"
    user = request.user
    pagina = Pagina.objects.all()
    template ="menu_paginas.html" 
    return render(request,template, locals())