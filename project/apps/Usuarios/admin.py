from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Empleado)


@admin.register(models.Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = (
        "usuario",
        "producto",
        "cantidad",
        "fecha_salida"
    )
    list_display_links = ("producto",)
    search_fields = ("producto.nombre", "usuario")
    list_filter = ("usuario",)
    date_hierarchy = "fecha_salida"