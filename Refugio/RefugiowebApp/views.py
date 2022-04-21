from cv2 import log
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from albergue.forms import DatosForm





def home(request):

    return render(request, "RefugiowebApp/Home.html")
@login_required
def servicios(request):

    return render(request, "RefugiowebApp/Servicios.html")

def contacto(request):

    return render(request, "RefugiowebApp/Contacto.html")

def formularioRegistro(request):
    data={
        'form':DatosForm()
    }
    if request.method=='POST':
        formulario=DatosForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Formulario Guardado"
        else:
            data["form"]=formulario

    return render(request, "RefugiowebApp/Formulario.html", data)





