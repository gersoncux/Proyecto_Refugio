from django.urls import path
from .views import registro, cerrar_sesion, logear



urlpatterns = [
 
    path('', registro, name="autentication"),

    path('cerrar_sesion', cerrar_sesion, name="log_out"),
    path('logear', logear, name="logear"),
]