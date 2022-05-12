from unicodedata import name
from django import views
from django.urls import path
from .views import ListaMascotasPdf, datos, agregar, eliminar_solicitud, modificar, listar, envio, eliminar_mascota
from .views import adopcion, listadopcion, modificarSol, ListaMascotasView, ListaMascotasPdf


urlpatterns = [

    path('', datos, name="Albergue"),
    path('agregar-mascota/',agregar, name="agregar"),
    path('modificar-mascota/<id>/', modificar, name="modificar_mascota"),
    path('listar-mascotas/', listar, name="listar"),
    path('agregar-mascota/send-it/', envio, name="enviado"),
    path('elimiar-mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),
    path('adoptar/', adopcion, name="adoptar" ),
    path('listado_adopcion/', listadopcion, name="list_adopcion"),
    path('modificar-solicitud/<id>/', modificarSol, name="modificar_solicitud"),
    path('elimiar-solicitud/<id>/', eliminar_solicitud, name="eliminar_solicitud"),
    path('lista_pdf/', ListaMascotasView.as_view(), name="lista_pdf"),
    path('Document/', ListaMascotasPdf.as_view(), name="documento"),

]

