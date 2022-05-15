from django.db import models
from django.conf import settings
import os

# function to get the path to the upload directory
def xoki_directory_path(instance, filename):
    imagen_name = 'xoki/media/{0}/{1}'.format(instance.nombre, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, imagen_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return imagen_name


# Create your models here.

class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    contratado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Jefe_Condominio(models.Model):
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Condomino(models.Model):
    jefe_Condominio = models.ForeignKey(Jefe_Condominio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_jefe  

class Vivienda(models.Model):
    condominio = models.ForeignKey(Condomino, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)


class Guardia(models.Model):
    condiminio = models.ForeignKey(Condomino, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    contratado = models.BooleanField(default=True)
    trabajando = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre





class Habitante(models.Model):
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estatus = models.BooleanField(default=True)
    duenio = models.BooleanField(default=False)
    foto = models.ImageField(upload_to=xoki_directory_path, blank=True, null=True)


    def __str__(self):
        return self.nombre

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



  






class Publicacion(models.Model):
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


