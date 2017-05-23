#encoding:utf-8
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import Multimedia

@login_required(login_url='/usuarios/login/')
def menu_multimedia(request):
	page_title = "MULTIMEDIAS"
	user = request.user
	multimedia = Multimedia.objects.all()
	template ="menu_multimedia.html"
	return render(request,template, locals())

@login_required(login_url='/usuarios/login/')
def agregar_multimedia(request):
	page_title = "AGREGAR MULTIMEDIA"
	user = request.user
	template ="agregar_multimedia.html"
	return render(request,template, locals())