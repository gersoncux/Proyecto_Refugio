from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from RefugiowebApp.forms import FormularioContacto



def home(request):

    return render(request, "RefugiowebApp/Home.html")

def servicios(request):

    return render(request, "RefugiowebApp/Servicios.html")

def albergue(request):

    return render(request, "RefugiowebApp/Albergue.html")

def contacto(request):

    return render(request, "RefugiowebApp/Contacto.html")

def formularioRegistro(request):

    return render(request, "RefugiowebApp/Formulario.html")

def sesion(request):

    return render(request, "RefugiowebApp/Sesion.html")


def contacto(request):

    if request.method=="POST":

        miFormulario=FormularioContacto(request.POST)

        if miFormulario.is_valid():
            
            infForm=miFormulario.cleaned_data

            send_mail(infForm['asunto'],infForm['mensaje'],
            infForm.get('email',''),['segundaoportunidadpaws@gmail.com'],)

            return render(request, "RefugiowebApp/gracias.html")

    else:
        miFormulario=FormularioContacto()
    return render(request, "formulario_contacto.html",{"form":miFormulario})


