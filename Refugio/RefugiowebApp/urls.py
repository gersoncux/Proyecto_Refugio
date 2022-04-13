from django.urls import path
from RefugiowebApp import views



urlpatterns = [
    path('', views.home, name="Home"),
    path('servicios/', views.servicios, name="Servicios"),
    path('Albergue/', views.albergue, name="Albergue"),
    path('Form_Reg/', views.formularioRegistro, name="FormularioRegistro"),
]