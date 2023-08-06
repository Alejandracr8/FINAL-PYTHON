from django.contrib import admin

from django.contrib import admin
from . import models

admin.site.register(models.Usuario)


@admin.register(models.Salida)
class SalidaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "numero_serie",
        "tipo_gas",
        "cantidad",
        "fecha_vsalida"
    )
    list_display_links = ("numero_serie",)
    search_fields = ("numero_serie", "nombre")
    list_filter = ("usuario",)
    date_hierarchy = "fecha_salida"
