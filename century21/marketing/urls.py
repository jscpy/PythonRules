from django.conf.urls import include, url, patterns
from django.contrib import admin

from marketing.views import Menu, ClientesListView, AsesorListView
from marketing import views

urlpatterns = [
    url(r'^$', Menu.as_view(),name='home'),
    url(r'^directorio/$', ClientesListView.as_view(),name='directorio'),
    url(r'^directorio/cliente/(?P<pk>\d+)/$', views.Cliente_detalles, name='cliente_detalles'),
    url(r'^asesores/$', AsesorListView.as_view(), name='asesores'),
    url(r'^asesores/detalles/(?P<pk>\d+)/$', views.Asesor_detalles, name='asesor_detalles'),
] 
