from django.shortcuts import render, get_object_or_404
from .models import Propiedad, Agente, Cliente
from django.http import JsonResponse
from django.views.generic import ListView, DetailView

def index(request):
    return render(request, 'index.html')

class PropiedadListView(ListView):
    model = Propiedad
    template_name = 'propiedades/lista.html'
    context_object_name = 'propiedades'

class PropiedadDetailView(DetailView):
    model = Propiedad
    template_name = 'propiedades/detalle.html'
    context_object_name = 'propiedad'

class AgenteListView(ListView):
    model = Agente
    template_name = 'agentes/lista.html'
    context_object_name = 'agentes'

class AgenteDetailView(DetailView):
    model = Agente
    template_name = 'agentes/detalle.html'
    context_object_name = 'agente'

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/lista.html'
    context_object_name = 'clientes'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/detalle.html'
    context_object_name = 'cliente'

def ajax_propiedad(request, id):
    propiedad = get_object_or_404(Propiedad, pk=id)
    return JsonResponse({
        "agente": propiedad.agente.nombre if propiedad.agente else "Sin agente",
        "cliente": propiedad.cliente.nombre if propiedad.cliente else "Sin cliente",
        "precio": propiedad.precio,
        "descripcion": propiedad.descripcion,
    })

def ajax_agente(request, id):
    agente = get_object_or_404(Agente, pk=id)
    return JsonResponse({
        "nombre": agente.nombre,
        "telefono": agente.telefono,
        "email": agente.email,
    })

def ajax_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    return JsonResponse({
        "nombre": cliente.nombre,
        "email": cliente.email,
        "telefono": cliente.telefono,
    })