from django.db import models
from xoki.models import Habitante

# Create your models here.
class Publicacion(models.Model):
    creado_por_el_habitante = models.ForeignKey(Habitante, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    creado_por_el_habitante = models.ForeignKey(Habitante, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contenido

class Respuesta(models.Model):
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)
    creado_por_el_habitante = models.ForeignKey(Habitante, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contenido
