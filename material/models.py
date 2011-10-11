# -*- coding: utf-8 -*-

from django.db import models
from asignaturas.models import Asignatura, Carrera
from smart_selects.db_fields import ChainedForeignKey
from usuarios.models import Usuario

class Archivo(models.Model):
    archivo = models.FileField(upload_to='material')
    creado = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=(('P', 'Publicado'), ('R', 'Revisión')))
    usuario = models.ForeignKey(Usuario, null=True, blank=True)

    asignatura = ChainedForeignKey(
        Asignatura,
        chained_field="carrera",
        chained_model_field="carrera",
        show_all=False,
        auto_choose=False
    )

    def __unicode__(self):
        return self.asignatura.carrera.universidad.abreviatura + '/' + self.asignatura.carrera.nombre + '/' + self.asignatura.abreviatura +'/' + self.archivo.name

    class Meta:
        verbose_name_plural = "material"

class Examen(Archivo):
    anno = models.IntegerField(verbose_name='Año')
    convocatoria = models.CharField(max_length=1, choices=(('F', 'Febrero'),('J', 'Junio'), ('S', 'Septiembre'),('D', 'Diciembre'),))
    solucion = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "examenes"
    
