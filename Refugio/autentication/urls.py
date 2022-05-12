from ast import For
from tokenize import Name
from unicodedata import name
from django.urls import path
from .views import  ChangePassword, registro, cerrar_sesion, logear, Ecorreo
from .views import ForgetPassword, modificar_user, listusuarios, eliminar_usuario, ListaUsuariosPdf



urlpatterns = [
 
    path('', registro, name="autentication"),

    path('cerrar_sesion', cerrar_sesion, name="log_out"),
    path('logear', logear, name="logear"),
    path('reset_password/', ForgetPassword, name="reset"),
    path('reset_Ecorreo/', Ecorreo, name="envio_correo"),
    path('change_password/<token>/',ChangePassword, name="change_password"),
    path('editar_perfil/<id>/', modificar_user, name="mod_user"),
    path('lista_usarios/', listusuarios, name="lista_usuarios"),
    path('elimiar-solicitud/<id>/', eliminar_usuario, name="eliminar_usuario"),
    #path('editar_usuario/<id>/', modificar_user_Admin, name="mod_userAdmin"),
    path('Doc/', ListaUsuariosPdf.as_view(), name="documento_pdf"), 
]
