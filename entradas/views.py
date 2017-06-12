#encoding:utf-8
from django.template.context_processors import csrf
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.contrib.auth.models import User
from usuarios.models import Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Categoria_Entrada,Comentario_Entrada,Etiqueta_Entrada,Entrada
from .forms import entradaForm

@login_required(login_url='/usuarios/login/')
def agregar_categoria(request):
    page_title = "AGREGAR CATEGORIA"
    user = request.user
    template ="agregar_cat_entrada.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_etiqueta(request):
    page_title = "AGREGAR ETIQUETA"
    user = request.user
    template ="agregar_eti_entrada.html" 
    return render(request,template, locals())

def agregar_comentario(request):
    page_title = "AGREGAR COMENTARIO"
    user = request.user
    template ="agregar_com_entrada.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_entrada(request):
    user = request.user
    usuario = Usuario.objects.get(usuario=user)
    etiqueta_entrada = Etiqueta_Entrada.objects.all()
    categoria_entrada = Categoria_Entrada.objects.all()
    comentario_entrada = Comentario_Entrada.objects.all()
    entrada = Entrada.objects.all()
    if request.method == 'POST':
        form_entrada = entradaForm(request.POST,request.FILES)
        if form_entrada.is_valid():
            entrada = form_entrada.save(commit=False)
            entrada.save()
            return redirect('menu-entradas')
    else:
        form_entrada = entradaForm()
    args = {}
    args.update(csrf(request))
    page_title = "AGREGAR ENTRADA"
    template ="agregar_entrada.html"
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def menu_entradas(request):
    page_title = "ENTRADAS"
    user = request.user
    entrada = Entrada.objects.all()
    template ="menu_entradas.html" 
    return render(request,template, locals())