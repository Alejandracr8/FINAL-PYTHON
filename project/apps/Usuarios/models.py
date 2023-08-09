from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

class Empleado(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="empleado")
    rut = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="usuarios", blank=True, null=True)

    def __str__(self):
        return self.usuario.username
    
