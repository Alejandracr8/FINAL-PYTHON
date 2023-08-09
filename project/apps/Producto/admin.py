from django.contrib import admin
from . import models

admin.site.site_title = "Producto"



@admin.register(models.Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion",)
    list_filter = ("nombre",)
    search_fields = ("nombre", "direccion",)
    ordering = ("nombre",)


@admin.register(models.Cilindro)
class CilindroAdmin(admin.ModelAdmin):
    list_display = (
        "numero_serie",
        "tipo_gas",
        "capacidad",
        "ubicacion",
        "fecha_ingreso",
    )
    list_display_links = ("numero_serie",)
    search_fields = ("numero_serie",)
    ordering = (
        "numero_serie",
        "tipo_gas",
    )
    list_filter = ("numero_serie",)
    date_hierarchy = "fecha_ingreso"


@admin.register(models.Salida)
class SalidaAdmin(admin.ModelAdmin):
    list_display = (
        "numero_serie",
        "tipo_gas",
        "capacidad",
        "ubicacion",
        "fecha_salida",
    )
    list_display_links = ("numero_serie",)
    search_fields = ("numero_serie",)
    ordering = (
        "numero_serie",
        "tipo_gas",
    )
    list_filter = ("numero_serie",)
    date_hierarchy = "fecha_salida"   