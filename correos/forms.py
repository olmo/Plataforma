from django import forms
from correos.models import Mensaje

class CorreoForm(forms.Form):
    receptor = forms.CharField()
    asunto = forms.CharField(max_length=50)
    texto = forms.CharField( widget=forms.Textarea )
