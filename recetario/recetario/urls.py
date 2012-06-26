from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^sobre/$','principal.views.sobre'),
    url(r'^$','principal.views.inicio'),
    url(r'^usuarios/$','principal.views.usuarios'),
    url(r'^recetas/$', 'principal.views.lista_recetas'),
    url(r'^receta/nueva/$', 'principal.views.nueva_receta'),
    url(r'^receta/(?P<id_receta>\d+)$','principal.views.detalle_receta'),
    url(r'^comenta/$', 'principal.views.nuevo_comentario'),
    url(r'^contacto/$', 'principal.views.contacto'),
    url(r'^usuario/nuevo$', 'principal.views.nuevo_usuario'),
	#url(r'^$','principal.views.lista_bebidas'),
    # Examples:
    # url(r'^$', 'recetario.views.home', name='home'),
    # url(r'^recetario/', include('recetario.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    			{'document_root':settings.MEDIA_ROOT,}
    	),
)
