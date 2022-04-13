from django.urls import path
from .views import VRegistro, cerrar_sesion, logear



urlpatterns = [
 
    path('', VRegistro.as_view(), name="autentication"),

    path('cerrar_sesion', cerrar_sesion, name="log_out"),
    path('logear', logear, name="logear"),
]