from django.db import models

# Create your models here.

class Dea(models.Model):
    codigo_dea = models.CharField(max_length=100) #VARCHAR
    direccion_ubicacion = models.CharField(max_length=100)
    direccion_via_nombre = models.CharField(max_length=100)
    direccion_portal_numero = models.CharField(max_length=100)
    horario_acceso = models.CharField(max_length=100)
    x_utm = models.IntegerField(default=None)
    y_utm = models.IntegerField(default=None)
    