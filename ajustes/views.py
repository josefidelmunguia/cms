#encoding:utf-8
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import Ajuste

@login_required(login_url='/usuarios/login/')
def menu_ajustes(request):
    page_title = "Menú Ajustes"
    user = request.user
    ajuste = Ajuste.objects.all()
    template ="menu_ajustes.html" 
    return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def ajustes(request):
    page_title = "Ajustes"
    user = request.user
    template ="ajustes.html" 
    return render(request,template, locals())

