from django.shortcuts import render




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





