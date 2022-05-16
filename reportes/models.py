from django.db import models
from xoki.models import Habitante

# Create your models here.





class Reporte(models.Model):
    creado_por_el_habitante = models.ForeignKey(Habitante, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    tipo_de_reporte = models.IntegerField()

    def __str__(self):
        return self.contenido

class Tipo_de_reporte(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
