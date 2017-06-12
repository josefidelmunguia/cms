#encoding:utf-8
from django.template.context_processors import csrf
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Ajuste
from .forms import ajusteForm

@login_required(login_url='/usuarios/login/')
def menu_ajustes(request):
    page_title = "AJUSTES"
    user = request.user
    ajuste = Ajuste.objects.all()
    template ="menu_ajustes.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def ajustes(request):    
    user = request.user
    ajuste = Ajuste.objects.all()
    if request.method == 'POST':
        form_ajuste = ajusteForm(request.POST)
        if form_ajuste.is_valid():
            ajuste = form_ajuste.save(commit=False)
            ajuste.save()
            return redirect('menu-ajustes')
    else:
        form_ajuste = ajusteForm()
    args = {}
    args.update(csrf(request))
    page_title = "AGREGAR AJUSTE"
    template ="ajustes.html" 
    return render(request,template, locals())