from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext, Context
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from ciapsse_web.models import *
from django.contrib.auth.models import User
# Create your views here.


def home(request):
#chequeo si hay imagenes para el carrusel, sino las creo	
	if not ImagenCarrusel.objects.filter().exists():
		imagenes_carrusel = []
		for i in range(4):
			img = ImagenCarrusel()
			img.save()
			imagenes_carrusel.append(img)
	else:
		imagenes_carrusel = ImagenCarrusel.objects.filter()[:4]		
# chequeo si hay contenido, sino lo creo		
	if not ContenidoGeneral.objects.get(pk = 1):
		contenido_general = ContenidoGeneral()
		contenido_general.save()
	
	else:
		contenido_general = ContenidoGeneral.objects.get(pk = 1)
		
		
	context = {
		"imagenes_carrusel": imagenes_carrusel,
		"contenido_general": contenido_general,
		"articulos":Articulo.objects.filter(is_active = True).order_by("-fecha")[:5]
	}
	template = render(request, "public/index.html", context)
	return template
	
def quienes_somos(request):
	context = {
		"integrantes":Integrantes.objects.filter(),
		"contenido_general": ContenidoGeneral.objects.get(pk = 1)
	}
	template = render(request, "public/quienes_somos.html",context)
	return template
	
def articulo_ver(request, id_articulo):
	context = {
		"articulo":Articulo.objects.get(pk = id_articulo)
	}
	template = render(request, "public/articulo_ver.html", context)
	return template
	

def admin(request):
	if request.user.is_authenticated():
		context = {
			"integrantes":Integrantes.objects.filter(),
			"contenido_general": ContenidoGeneral.objects.get(pk = 1),
			"imagenes_carrusel":ImagenCarrusel.objects.filter()[:4],
			"articulos":Articulo.objects.filter(is_active = True).order_by("-fecha")
		}
		template = render(request, "private/admin.html", context)
		return template
	else:
		return redirect("ciapsse_web:home")


def articulo_crear(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			articulo = Articulo()
			articulo.titulo = request.POST['titulo']
			articulo.contenido = request.POST['contenido']
			try: 
				request.FILES['imagen']
				articulo.imagen = request.FILES['imagen']                
			except: pass
			
			articulo.save()	 
			return redirect("ciapsse_web:admin")
		else:
			template = render(request, "private/articulo_form.html")
			return template
	else:
		return redirect("ciapsse_web:home")

def articulo_editar(request, id_articulo):
	if request.user.is_authenticated():
		articulo = Articulo.objects.get(pk = id_articulo)
		context = {
			"articulo":articulo
		}
		if request.method == 'POST':
			articulo.titulo = request.POST['titulo']
			articulo.contenido = request.POST['contenido']
			try: 
				request.FILES['imagen']
				articulo.imagen = request.FILES['imagen']                
			except: pass
			
			articulo.save()	 
			return redirect("ciapsse_web:admin")
		else:
			template = render(request, "private/articulo_form.html", context)
			return template
	else:
		return redirect("ciapsse_web:home")


def articulo_desactivar(request, id_articulo):
	if request.user.is_authenticated():
		articulo = Articulo.objects.get(pk = id_articulo)
		articulo.is_active = False
		articulo.save()
		return redirect("ciapsse_web:admin")
	else:
		return redirect("ciapsse_web:home")
		
def carrusel_editar(request, id_imagen):
	if request.user.is_authenticated():
		imagen = ImagenCarrusel.objects.get(pk = id_imagen)
		if request.method == 'POST':
			print request.POST['slogan']
			print request.POST['titulo']
			imagen.titulo = request.POST['titulo']
			
			imagen.slogan = request.POST['slogan']
			try: 
				request.FILES['imagen']
				imagen.imagen = request.FILES['imagen']                
			except: pass
			
			imagen.save()	 
			return redirect("ciapsse_web:admin")
		else:
			return redirect("ciapsse_web:admin")
	else:
		return redirect("ciapsse_web:home")

def texto_pag_principal_editar(request):
	if request.user.is_authenticated():
		contenido_general = ContenidoGeneral.objects.get(pk = 1)
		if request.method == 'POST':
			contenido_general.main_pagina_principal = request.POST['texto']
			contenido_general.titulo_pagina_principal = request.POST['titulo']
			contenido_general.save()	 
			return redirect("ciapsse_web:admin")
		else:
			return redirect("ciapsse_web:admin")
	else:
		return redirect("ciapsse_web:home")
		
# ################## SISTEMA DE AUTENTICACION ##################
def login_user(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            # the password verified for the user
            if user.is_active:
				login(request, user)
				return redirect("ciapsse_web:admin")
				
            else:
                print("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            print("The username and password were incorrect.")
    else:
        return render(request, "private/login.html")


def logout_user(request):
	logout(request)
	return redirect("ciapsse_web:home")