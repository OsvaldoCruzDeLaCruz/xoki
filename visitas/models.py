from django.db import models
from django.conf import settings
import os
from xoki.models import Habitante, Vivienda

# A function to get the path to the upload directory for the image QR
def qr_directory_path(instance, filename):
    imagen_name = 'xoki/media/qrs/{0}/{1}'.format(instance.nombre_del_visitante, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, imagen_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return imagen_name



# Create your models here.
class Visita(models.Model):
    creado_por_el_habitante = models.ForeignKey(Habitante, on_delete=models.CASCADE)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    nombre_del_visitante = models.CharField(max_length=100)
    apellido_del_visitante = models.CharField(max_length=100)
    correo_del_visitante = models.EmailField()
    telefono_del_visitante = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    comentario = models.TextField()
    estatus = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    codigo_qr = models.ImageField(upload_to=qr_directory_path, null=True, blank=True)
    # tiempo_de_expiracion = models.DateTimeField(models.DateTimeField(auto_now_add=True)) Falta colocar el tiempo de expiracion

    def __str__(self):
        return self.nombre_del_visitante

