from email.message import EmailMessage
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from django.conf import settings
from contactoApp.forms import FormularioContacto
from django.contrib import messages

# Create your views here.

def contacto(request):
    miFormulario=FormularioContacto()

    if request.method=="POST":

        miFormulario=FormularioContacto(data=request.POST)

        if miFormulario.is_valid():
            
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde App Django",
            "El usuario {} con la direccion {} escribe lo siguiente \n\n {}".format(nombre,email,contenido),
            "",["segundaoportunidadpaws@gmail.com"], reply_to=[email])

            try:

                email.send()
                messages.success(request, "Enviado correctamente! Gracias por contactarnos!")
            
            except:

                return redirect("/contacto/?novalido")

    else:
        miFormulario=FormularioContacto()
    return render(request, "contacto/formulario_contacto.html",{"form":miFormulario})
