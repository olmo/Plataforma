from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from asignaturas.models import Carrera

class Usuario(models.Model):
    user = models.OneToOneField(User)

    carreras = models.ManyToManyField(Carrera)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Usuario.objects.create(user=instance)
    
    post_save.connect(create_user_profile, sender=User)