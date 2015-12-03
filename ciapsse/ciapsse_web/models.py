from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
from datetime import *
from django.utils.safestring import SafeUnicode

# Create your models here.
class Articulo(models.Model):
	is_active = models.BooleanField(default=True)
	fecha = models.DateField(default=timezone.now)
	titulo = models.CharField(max_length=40)
	contenido = models.TextField()
	imagen = models.ImageField(upload_to='imagenes_articulo', blank=True)
	
	def __unicode__(self):
		return self.titulo
	
	def es_de_hoy(fecha):
		if fecha == timezone.now:
			return True
		else:
			return False	
			
	class Meta:
		verbose_name = 'articulo'
		verbose_name_plural = 'articulos'
		
class ImagenCarrusel(models.Model):
	titulo = models.CharField(max_length=40)
	slogan = models.CharField(max_length=40)
	imagen = models.ImageField(upload_to='imagenes_carrusel', blank=True)
	
	def __unicode__(self):
		return self.titulo
	
	class Meta:
		verbose_name = 'imagen_carrusel'
		verbose_name_plural = 'imagenes_carrusel'
		
class ContenidoGeneral(models.Model):
	titulo_pagina_principal = models.CharField(max_length = 40, blank=True)
	main_pagina_principal = models.TextField(blank=True)
	main_quienes_somos = models.TextField(blank=True)
	mail_contacto = models.CharField(max_length = 40, blank=True)
	facebook = models.CharField(max_length = 60, blank=True)
	
	def __unicode__(self):
		return "contenido_general(variable unica)"
	
	class Meta:
		verbose_name = 'contenido_general(variable unica)'
		verbose_name_plural = 'contenido_general(variable unica)'
		
class Integrantes(models.Model):
	foto = models.ImageField(upload_to='imagenes_integrantes', blank=True)
	nombre = models.CharField(max_length = 40)
	apellido = models.CharField(max_length = 40)
	prefijo = models.CharField(max_length = 10)
	cv = models.TextField()
	mail = models.CharField(max_length = 40, blank=True)
	
	def __unicode__(self):
		return self.prefijo+" "+self.nombre+" "+self.apellido
	
	class Meta:
		verbose_name = 'integrante'
		verbose_name_plural = 'integrantes'
		