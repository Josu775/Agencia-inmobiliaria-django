from django.contrib import admin
from .models import Agente, Cliente, Propiedad

# ADMIN DE AGENTE
@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "telefono")
    search_fields = ("nombre", "email")
    list_filter = ("telefono",)
    ordering = ("nombre",)

# ADMIN DE CLIENTE
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "telefono")
    search_fields = ("nombre", "email")
    list_filter = ("telefono",)
    ordering = ("nombre",)

# ADMIN DE PROPIEDAD
@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ("direccion", "precio", "agente", "cliente")
    search_fields = ("direccion", "descripcion")
    list_filter = ("agente", "cliente", "precio")
    ordering = ("precio",)

    readonly_fields = ("precio",)
