from django.db import models

class Universidad(models.Model):
    nombre = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=10)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    universidad = models.ForeignKey(Universidad, related_name='carrera_uni')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "carreras"
        ordering = ['nombre']

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=10)
    carrera = models.ForeignKey(Carrera, related_name='asign_carrera')
    curso = models.IntegerField()

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "asignaturas"
