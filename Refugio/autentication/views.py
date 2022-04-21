import profile
import django
from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .helpers import send_forget_password_mail
from .models import Profile
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required


################## Create your views here. #################################

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


import uuid
def ForgetPassword(request):
    try:
        if request.method=='POST':
            username=request.POST.get('username')

            if not User.objects.filter(username=username).first():
                messages.success(request, 'Nor user found with this username.')
                return redirect('reset')

            user_obj = User.objects.get(username=username)
            token=str(uuid.uuid4())
            profile_obj=Profile.objects.get(user=user_obj)
            profile_obj.forget_password_token=token
            profile_obj.save()
            send_forget_password_mail(user_obj, token)
            messages.success(request, 'An email is sent.')
            print("El email, fue enviado correctamente!!!")
            return render(request, 'login/Ecorreo.html' )
    except Exception as e:
        print(e)
        print("error")
    return render(request, 'login/resetear.html')

def Ecorreo(request):
    return render(request, 'login/Ecorreo.html')


def ChangePassword(request, token):
    context={}
    try:
        profile_obj=Profile.objects.filter(forget_password_token=token).first()
        context={'user_id':profile_obj.user.id}
        print(profile_obj)

        if request.method=='POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')

            if user_id is None:
                messages.success(request, 'No user id found.')
                return redirect(f'change_password/{token}/')

            if new_password != confirm_password:
                messages.success(request, 'Deben ser iguales')
                return redirect(f'change_password/{token}/')
            
            user_obj = User.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('logear')

            
  
    except Exception as e:
        print(e)
    return render(request, 'login/Change.html')


def modificar_user(request, id):
    
    usuario = get_object_or_404(User, id=id)

    data={
        'form':CustomUserCreationForm(instance=usuario)
    }

    if request.method=='POST':
        formulario=CustomUserCreationForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Parametro Modificado")
            #Redireccionar al Home
            return redirect(to="Home")
        data["form"]=formulario

    return render(request, 'lista/mod_user.html', data)

@permission_required('auth.view_user')
def listusuarios(request):
    usuarios = User.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(usuarios, 5)
        usuarios = paginator.page(page)
    except:
        raise Http404


    data={
        'entity': usuarios,
        'paginator': paginator
    }

    return render(request, 'lista/list_user.html', data)

@permission_required('auth.delete_user')
def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    usuario.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="lista_usuarios")

'''
def modificar_user_Admin(request, id):
    
    usuario = get_object_or_404(User, id=id)

    data={
        'form':ModUserAdmin(instance=usuario)
    }

    if request.method=='POST':
        formulario=ModUserAdmin(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Parametro Modificado")
            #Redireccionar al Home
            return redirect(to="Home")
        data["form"]=formulario
'''
