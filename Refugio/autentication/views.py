from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib import messages


# Create your views here.

def registro(request):
    data={
        'form':CustomUserCreationForm()
    }

    if request.method=='POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            #Redireccionar al Home
            return redirect(to="Home")
        else:
            for msg in formulario.error_messages:
                messages.error(request, formulario.error_messages[msg])
            return render(request, "registro/Sesion.html",{"form":formulario})
    return render(request, 'registro/Sesion.html', data)


def cerrar_sesion(request):
    logout(request)

    return redirect('Home')

def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "usuario no valido")
        else:
            messages.error(request, "informacion incorrecta")
            
    form=AuthenticationForm()
    return render(request, "login/login.html",{"form":form})