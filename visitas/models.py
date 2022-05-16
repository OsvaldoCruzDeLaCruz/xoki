from django.db import models
from xoki.models import Habitante

# Create your models here.
class Visita(models.Model):
    creado_por_el_habitante = models.ForeignKey(Habitante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    comentario = models.TextField()
    estatus = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    # tiempo_de_expiracion = models.DateTimeField(models.DateTimeField(auto_now_add=True)) Falta colocar el tiempo de expiracion

    def __str__(self):
        return self.nombre

