from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('propiedades/', views.lista_propiedades, name='lista_propiedades'),
    path('propiedades/<int:id>/', views.detalle_propiedad, name='detalle_propiedad'),

    path('agentes/', views.lista_agentes, name='lista_agentes'),
    path('agentes/<int:id>/', views.detalle_agente, name='detalle_agente'),

    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/<int:id>/', views.detalle_cliente, name='detalle_cliente'),
]
