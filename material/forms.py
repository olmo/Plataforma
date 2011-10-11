from django import forms
from smart_selects.form_fields import ChainedModelChoiceField
from asignaturas.models import Universidad

class FiltroForm(forms.Form):
    universidad = forms.ModelChoiceField(queryset=Universidad.objects.all())
    carrera = ChainedModelChoiceField(app_name='asignaturas', auto_choose=False, chain_field='universidad', model_field='universidad', model_name='carrera', show_all=False)
    asignatura = ChainedModelChoiceField(app_name='asignaturas', auto_choose=False, chain_field='carrera', model_field='carrera', model_name='asignatura', show_all=False)