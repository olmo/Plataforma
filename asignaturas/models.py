from django.db import models

class Asignatura(models.Model):
    nombre = models.CharField(max_length=200)
