from django.conf.urls import include, url


urlpatterns = [
	
	url(r'^$', 'ciapsse_web.views.home', name='home'),
	url(r'^logout/$', 'ciapsse_web.views.logout_user', name='logout'),
	url(r'^login/$', 'ciapsse_web.views.login_user', name='login'),
	url(r'^admin/$', 'ciapsse_web.views.admin', name='admin'),
	url(r'^quienes_somos/$', 'ciapsse_web.views.quienes_somos', name='quienes_somos'),
	url(r'^articulo_crear/$', 'ciapsse_web.views.articulo_crear', name='articulo_crear'),
	url(r'^articulo_editar/(?P<id_articulo>\d+)$', 'ciapsse_web.views.articulo_editar', name='articulo_editar'),
	url(r'^articulo_desactivar/(?P<id_articulo>\d+)$', 'ciapsse_web.views.articulo_desactivar', name='articulo_desactivar'),
	url(r'^(?P<id_articulo>\d+)$', 'ciapsse_web.views.articulo_ver', name='articulo_ver'),
	url(r'^carrusel_editar/(?P<id_imagen>\d+)$', 'ciapsse_web.views.carrusel_editar', name='carrusel_editar'),
	url(r'^texto_pag_principal_editar$', 'ciapsse_web.views.texto_pag_principal_editar', name='texto_pag_principal_editar'),
	
]