from django.urls import path

from . import views

app_name = "Producto"

urlpatterns = [path("", views.index, name="home")]

urlpatterns += [
    path("ubicacion/list/", views.UbicacionList.as_view(), name="ubicacion_list"),
    path("ubicacion/create/", views.UbicacionCreate.as_view(), name="ubicacion_create"),
    path("ubicacion/detail/<int:pk>", views.UbicacionDetail.as_view(), name="ubicacion_detail"),
    path("ubicacion/update/<int:pk>", views.UbicacionUpdate.as_view(), name="ubicacion_update"),
    path("ubicacion/delete/<int:pk>", views.UbicacionDelete.as_view(), name="ubicacion_delete"),
]

urlpatterns += [
    path("cilindro/list/", views.CilindroList.as_view(), name="cilindro_list"),
    path("cilindro/create/", views.CilindroCreate.as_view(), name="cilindro_create"),
    path("cilindro/detail/<int:pk>", views.CilindroDetail.as_view(), name="cilindro_detail"),
    path("cilindro/update/<int:pk>", views.CilindroUpdate.as_view(), name="cilindro_update"),
    path("cilindro/delete/<int:pk>", views.CilindroDelete.as_view(), name="cilindro_delete"),
]