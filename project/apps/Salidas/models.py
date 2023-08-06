from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class Usuario(models.Model):
    nombre = models.OneToOneField(User, on_delete=models.CASCADE, related_name="usuario")
    id = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)

    def __str__(self):
        return self.nombre.username


class Salida(models.Model):
    nombre = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    numero_serie = models.CharField("Producto.Cilindro", on_delete=models.CASCADE)
    tipo_gas = models.CharField(max_length=50)
    cantidad = models.PositiveIntegerField()
    fecha_salida = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ("-fecha_salida",)

    def clean(self):
        if self.cantidad > self.numero_serie.cantidad:
            raise ValidationError("La cantidad vendida no puede ser mayor a la cantidad disponible")

  