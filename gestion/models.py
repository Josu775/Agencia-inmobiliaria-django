from django.db import models

class Agente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='agentes/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='clientes/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Propiedad(models.Model):
    direccion = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(upload_to='propiedades/', null=True, blank=True)

    def __str__(self):
        return self.direccion
