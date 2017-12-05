from django.conf.urls import url,include
from django.contrib import admin
from libros import views
from libros.views import (ListaDeCarros, DetalleDeCarros, CrearCarros, ActualizarCarros)
from accounts.views import UserRegisterView

urlpatterns = [
    url(r'^(?P<pk>\d+)/editar/$', ActualizarCarros.as_view(), name='actualizar'),
    url(r'^(?P<pk>\d+)/$', DetalleDeCarros.as_view(), name='detalle'),
    url(r'^crear/$', CrearCarros.as_view(), name='crear'),
    url(r'^lista/$', ListaDeCarros.as_view(), name='lista'),
    url(r'^(?P<slug>[\w-]+)/$', DetalleDeCarros.as_view(), name='detalle_slug'),

]
