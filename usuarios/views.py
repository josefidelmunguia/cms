#encoding:utf-8
from django.template.context_processors import csrf
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario,Perfil
from .forms import registerForm,comp1Form,comp2Form

def login(request):
    if not request.user.is_anonymous():
        return redirect('index')
    if request.POST:
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    auth.login(request, acceso)
                    return redirect('index')
    page_title = "INICIO DE SESIÓN"
    user = request.user
    template ="login.html" 
    return render(request,template, locals())

def registrar_usuario(request):    
    user = request.user
    usuario = User.objects.all()    
    if request.method == 'POST':
        form_user = registerForm(request.POST)
        if form_user.is_valid():
            usuario = form_user.save(commit=False)
            usuario.save()
            return redirect('completar')
    else:
        form_user = registerForm()
    args = {}
    args.update(csrf(request))
    page_title = "REGISTRAR USUARIO"
    template ="registrar_usuario.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def completar_informacion(request):
    user = request.user
    usuario = Usuario.objects.get(usuario=user)
    comp1 = User.objects.all()
    perfil = Perfil.objects.all()    
    if request.method == 'POST':
        form1 = comp1Form(request.POST,instance=usuario)
        #form1 = comp1Form(request.POST)
        if form1.is_valid():
            comp1 = form1.save(commit=False)
            comp1.save()
            return redirect('index')
    else:
        form1 = comp1Form(request.POST,instance=usuario)
        #form1 = comp1Form(request.POST)
    args = {}
    args.update(csrf(request))
    page_title = "PASO 2"
    template ="completar.html" 
    return render(request,template, locals())
    
@login_required(login_url='/usuarios/login/')
def menu_usuarios(request):
    page_title = "USUARIOS"
    user = request.user
    usuarios = Usuario.objects.all()
    template ="menu_usuarios.html" 
    return render(request,template, locals())

#@login_required(login_url='/usuarios/login/')
#def menu_usuarios(request):
#    page_title = "USUARIOS"
#    user = request.user
#    users = User.objects.all()
#    usuarios = Usuario.objects.filter(user=users)
#    query = request.GET.get('q', '')
#    if query:
#        qset = (
#            Q(user=query) 
#        )    
#        results = Usuario.objects.filter(qset).order_by('-id')
#        template = "usuarios-resultado.html"
#        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
#    else:
#        results = []   
#    template ="menu_usuarios.html" 
#    return render_to_response(template, locals(),context_instance=RequestContext(request))   