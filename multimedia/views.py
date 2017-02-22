#encoding:utf-8
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/usuarios/login/')
def agregar_multimedia(request):
	page_title = "Agregar Multimedia"
	user = request.user
	template ="agregar_multimedia.html"
	return render(request,template, locals())