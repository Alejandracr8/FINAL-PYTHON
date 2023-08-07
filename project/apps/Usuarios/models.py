from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

class Empleado(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="vendedor")
    rut = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)

    def __str__(self):
        return self.usuario.username
    
class Registro(models.Model):
    usuario = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey("Producto.Cilindro", on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField()
    
    fecha_salida = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ("-fecha_salida",)

    def clean(self):
        if self.cantidad > self.producto.cantidad:
            raise ValidationError("La cantidad vendida no puede ser mayor a la cantidad disponible")

