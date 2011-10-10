from django.db import models
from usuarios.models import Usuario

class Mensaje(models.Model):
	remitente = models.ForeignKey(Usuario)
	receptor = models.ManyToManyField(Usuario, related_name='receptor_correo')
	asunto = models.CharField(max_length=50)
	texto = models.TextField()
	adjunto = models.FileField(upload_to='correos')
	fecha = models.DateField()
	
	class Meta:
		verbose_name_plural = "Mensajes"
