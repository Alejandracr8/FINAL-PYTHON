from django.db import models
from django.utils import timezone

# Create your models here.


class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
   
    def __str__(self):
        return f'{self.nombre} {self.direccion}'

class Cilindro(models.Model):
    numero_serie = models.CharField(max_length=100, unique=True)
    tipo_gas = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE) 
    fecha_ingreso = models.DateTimeField(
        default=timezone.now, verbose_name="fecha de ingreso") 
    
    def __str__(self) -> str:
        return f"{self.numero_serie} {self.tipo_gas}{self.ubicacion}"
    
    class Meta:
        verbose_name = "cilindro"
        verbose_name_plural = "cilindros"