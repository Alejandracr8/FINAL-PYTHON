from django import forms

from . import models


class UbicacionForm(forms.ModelForm):
    class Meta:
        model = models.Ubicacion
        fields = "__all__"


class CilindroForm(forms.ModelForm):
    class Meta:
        model = models.Cilindro
        fields = "__all__"