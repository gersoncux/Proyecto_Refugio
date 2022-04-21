from ast import For
from tokenize import Name
from unicodedata import name
from django.urls import path
from .views import  ChangePassword, registro, cerrar_sesion, logear, Ecorreo
from .views import ForgetPassword, modificar_user, listusuarios



urlpatterns = [
 
    path('', registro, name="autentication"),

    path('cerrar_sesion', cerrar_sesion, name="log_out"),
    path('logear', logear, name="logear"),
    path('reset_password/', ForgetPassword, name="reset"),
    path('reset_Ecorreo/', Ecorreo, name="envio_correo"),
    path('change_password/<token>/',ChangePassword, name="change_password"),
    path('editar_perfil/<id>/', modificar_user, name="mod_user"),
    path('lista_usarios/', listusuarios, name="lista_usuarios")
]
