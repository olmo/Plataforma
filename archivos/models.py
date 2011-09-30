# -*- coding: utf-8 -*-

from django.db import models
from asignaturas.models import Asignatura, Carrera
from smart_selects.db_fields import ChainedForeignKey

class Archivo(models.Model):
    archivo = models.FileField(upload_to='archivos')

    asignatura = ChainedForeignKey(
        Asignatura,
        chained_field="carrera",
        chained_model_field="carrera",
        show_all=False,
        auto_choose=False
    )

    def __unicode__(self):
        return self.archivo.name

    class Meta:
        verbose_name_plural = "archivos"

class Examen(Archivo):
    anno = models.IntegerField(verbose_name='Año')
    convocatoria = models.CharField(max_length=1, choices=(('F', 'Febrero'),('S', 'Septiembre'),('D', 'Diciembre'),))
    solucion = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "examenes"
    
