#encoding:utf-8
from django.template.context_processors import csrf
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.contrib.auth.models import User
from .models import Usuario
from .forms import registerUserForm

def login(request):
    page_title = "INICIO DE SESIÓN"
    user = request.user
    template ="login.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def registrar_usuario(request):    
    user = request.user
    usuario = User.objects.all()    
    if request.method == 'POST':
        form_user = registerUserForm(request.POST)
        if form_user.is_valid():
            usuario = form_user.save(commit=False)
            usuario.save()
            return redirect('index')
    else:
        form_user = registerUserForm()
    args = {}
    args.update(csrf(request))
    page_title = "REGISTRAR USUARIO"
    template ="registrar_usuario.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def menu_usuarios(request):
    page_title = "USUARIOS"
    user = request.user
    usuarios = Usuario.objects.all()
    template ="menu_usuarios.html" 
    return render(request,template, locals())