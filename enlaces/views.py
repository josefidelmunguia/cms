#encoding:utf-8
from django.template.context_processors import csrf
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Menu,Pagina,Categoria_Producto,Categoria_Entrada,Enlace
from .forms import enlaceForm

@login_required(login_url='/usuarios/login/')
def menu_enlaces(request):
    page_title = "ENLACES"
    user = request.user
    enlace = Enlace.objects.all()
    template ="menu_enlaces.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_menu(request):
    page_title = "AGREGAR MENÚ"
    user = request.user
    template ="agregar_menu.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_enlace(request):
    user = request.user
    pagina = Pagina.objects.all()
    categoria_producto = Categoria_Producto.objects.all()
    categoria_entrada = Categoria_Entrada.objects.all()
    menu = Menu.objects.all()
    enlace = Enlace.objects.all()
    if request.method == 'POST':
        form_enlace = enlaceForm(request.POST)
        if form_enlace.is_valid():
            enlace = form_enlace.save(commit=False)
            enlace.save()
            return redirect('menu-enlaces')
    else:
        form_ajuste = enlaceForm()
    args = {}
    args.update(csrf(request))
    page_title = "AGREGAR ENLACE"
    template ="agregar_enlace.html" 
    return render(request,template, locals())