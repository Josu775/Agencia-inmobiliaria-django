from django.shortcuts import render, get_object_or_404
from .models import Propiedad, Agente, Cliente

def index(request):
    return render(request, 'index.html')

def lista_propiedades(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'propiedades/lista.html', {'propiedades': propiedades})

def detalle_propiedad(request, id):
    propiedad = get_object_or_404(Propiedad, pk=id)
    return render(request, 'propiedades/detalle.html', {'propiedad': propiedad})

def lista_agentes(request):
    agentes = Agente.objects.all()
    return render(request, 'agentes/lista.html', {'agentes': agentes})

def detalle_agente(request, id):
    agente = get_object_or_404(Agente, pk=id)
    return render(request, 'agentes/detalle.html', {'agente': agente})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista.html', {'clientes': clientes})

def detalle_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    return render(request, 'clientes/detalle.html', {'cliente': cliente})
