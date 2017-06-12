#encoding:utf-8
from django.template.context_processors import csrf
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import auth
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Multimedia,Usuario
from .forms import multimediaForm

@login_required(login_url='/usuarios/login/')
def menu_multimedia(request):
	page_title = "MULTIMEDIAS"
	user = request.user
	multimedia = Multimedia.objects.all()
	template ="menu_multimedia.html"
	return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_multimedia(request):
    user = request.user
    usuario = Usuario.objects.get(usuario=user)
    multimedia = Multimedia.objects.all()
    if request.method == 'POST':
        form_multimedia = multimediaForm(request.POST,request.FILES)
        if form_multimedia.is_valid():
            multimedia = form_multimedia.save(commit=False)
            multimedia.save()
            return redirect('menu-multimedia')
    else:
        form_multimedia = multimediaForm()
    args = {}
    args.update(csrf(request))
    page_title = "AGREGAR MULTIMEDIA"
    template ="agregar_multimedia.html"
    return render(request,template, locals())