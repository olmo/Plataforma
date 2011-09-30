from archivos.models import Examen, Archivo
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from asignaturas.models import Carrera, Universidad
from smart_selects.form_fields import ChainedModelChoiceField

class ExamenForm(ModelForm):
    universidad = forms.ModelChoiceField(queryset=Universidad.objects.all())
    carrera = ChainedModelChoiceField(app_name='asignaturas', auto_choose=False, chain_field='universidad', model_field='universidad', model_name='carrera', show_all=False)
    
    class Meta:
        model = Examen
    

class ExamenAdmin(admin.ModelAdmin):
    form = ExamenForm
    fields = ['universidad', 'carrera', 'asignatura', 'anno', 'convocatoria', 'archivo', 'solucion']

admin.site.register(Archivo)
admin.site.register(Examen, ExamenAdmin)