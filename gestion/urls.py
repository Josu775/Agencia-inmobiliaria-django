from django.urls import path
from . import views

from .views import (
    PropiedadListView, PropiedadDetailView,
    AgenteListView, AgenteDetailView,
    ClienteListView, ClienteDetailView
)

urlpatterns = [
    path('', views.index, name='index'),

    path('propiedades/', PropiedadListView.as_view(), name='lista_propiedades'),
    path('propiedades/<int:pk>/', PropiedadDetailView.as_view(), name='detalle_propiedad'),

    path('agentes/', AgenteListView.as_view(), name='lista_agentes'),
    path('agentes/<int:pk>/', AgenteDetailView.as_view(), name='detalle_agente'),

    path('clientes/', ClienteListView.as_view(), name='lista_clientes'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='detalle_cliente'),

    path('ajax/propiedad/<int:id>/', views.ajax_propiedad, name='ajax_propiedad'),
    path('ajax/agente/<int:id>/', views.ajax_agente, name='ajax_agente'),
    path('ajax/cliente/<int:id>/', views.ajax_cliente, name='ajax_cliente'),

]
