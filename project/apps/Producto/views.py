from django.shortcuts import render
from typing import Any
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models


@login_required
def index(request):
    return render(request, "Producto/index.html")



class UbicacionList(ListView):
    model = models.Ubicacion

class UbicacionCreate(CreateView):
    model = models.Ubicacion
    form_class = forms.UbicacionForm
    success_url = reverse_lazy("Producto:ubicacion_list")

class UbicacionDetail(DetailView):
    model = models.Ubicacion

class UbicacionUpdate(UpdateView):
    model = models.Ubicacion
    form_class = forms.UbicacionForm
    success_url = reverse_lazy("Producto:ubicacion_list")

class UbicacionDelete(DeleteView):
    model = models.Ubicacion
    success_url = reverse_lazy("Producto:ubicacion_list")

#CILINDROS
class CilindroList(ListView):
    model = models.Cilindro

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Cilindro.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Cilindro.objects.all()
        return object_list


class CilindroCreate(CreateView):
    model = models.Cilindro
    form_class = forms.CilindroForm
    success_url = reverse_lazy("Producto:cilindro_list")


class CilindroDetail(DetailView):
    model = models.Cilindro


class CilindroUpdate(UpdateView):
    model = models.Cilindro
    form_class = forms.CilindroForm
    success_url = reverse_lazy("Producto:cilindro_list")


class CilindroDelete(DeleteView):
    model = models.Cilindro
    success_url = reverse_lazy("Producto:cilindro_list")


class CilindroList(ListView):
    model = models.Cilindro

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Cilindro.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Cilindro.objects.all()
        return object_list

#SALIDA
class SalidaCreate(CreateView):
    model = models.Salida
    form_class = forms.SalidaForm
    success_url = reverse_lazy("Producto:salida_list")


class SalidaDetail(DetailView):
    model = models.Salida


class SalidaUpdate(UpdateView):
    model = models.Salida
    form_class = forms.SalidaForm
    success_url = reverse_lazy("Producto:salida_list")


class SalidaDelete(DeleteView):
    model = models.Salida
    success_url = reverse_lazy("Producto:salida_list")
