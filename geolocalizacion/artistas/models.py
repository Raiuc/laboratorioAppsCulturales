from django.db import models

class Artista(models.Model):
    nombre     = models.CharField(max_length=30)
    apellido_p = models.CharField(max_length=30)
    apellido_m = models.CharField(max_length=30)

class Programador(models.Model):
    nombre     = models.CharField(max_length=30)
    apellido_p = models.CharField(max_length=30)
    apellido_m = models.CharField(max_length=30)

class Coleccionista(models.Model):
    nombre     = models.CharField(max_length=30)
    apellido_p = models.CharField(max_length=30)
    apellido_m = models.CharField(max_length=30)

class Lugar(models.Model):
    nombre     = models.CharField(max_length=30)
    longitud   = models.IntegerField()
    latitud    = models.IntegerField()

class Pieza(models.Model):
    nombre           = models.CharField(max_length=30)
    descripcion      = models.CharField(max_length=30)
    tecnica          = models.CharField(max_length=30)
    year             = models.IntegerField()
    artista          = models.ForeignKey(Artista)
    coleccionista    = models.ForeignKey(Coleccionista)
