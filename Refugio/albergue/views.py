from dataclasses import dataclass
from django.views import View
from django.views.generic import ListView
from urllib.request import Request
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from sympy import content

from .utils import render_to_pdf
from .models import Mascota, Adopcion
from RefugiowebApp.models import Datos
from .forms import MascotaForm, AdopcionForm, AdopcionAdminForm, MascotaAddForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def datos(request):

    mascotas=Mascota.objects.all()

    return render(request, "albergue/Albergue.html", {"mascotas": mascotas})


@login_required
@permission_required('albergue.add_mascota')
def agregar(request):

    data={
        'form': MascotaAddForm()
    }
    if request.method=='POST':
        formulario=MascotaAddForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro de mascota exitoso!")

        else:
            data["form"]=formulario
    return render(request, "tablas/agregar.html", data)


@login_required
def listar(request):
    mascotas = Mascota.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(mascotas, 5)
        mascotas = paginator.page(page)
    except:
        raise Http404


    data={
        'entity': mascotas,
        'paginator': paginator
    }

    return render(request, "tablas/listar.html", data)


@login_required
def envio(request):

    return render( request, "tablas/envio.html")



@permission_required('albergue.change_mascota')
def modificar(request, id):
    
    mascota = get_object_or_404(Mascota, id=id)

    data={
        'form': MascotaForm(instance=mascota)
    }
    if request.method=='POST':
        formulario=MascotaForm(data=request.POST, instance=mascota, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar")
        data["form"]=formulario

    return render(request, "tablas/modificar.html", data)


@permission_required('albergue.delete_mascota')
def eliminar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    mascota.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar")

@login_required
def adopcion(request):
    data={
        'form': AdopcionForm()
    }
    if request.method=='POST':
        formulario=AdopcionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Solicitud enviada")
        else:
            data["form"]=formulario

    return render(request, "tablas/adopcion.html",data)

@login_required
def listadopcion(request):
    solicitud = Adopcion.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(solicitud, 5)
        solicitud = paginator.page(page)
    except:
        raise Http404


    data={
        'entity': solicitud,
        'paginator': paginator
    }

    return render(request, "tablas/listaradopcion.html", data)

@permission_required('albergue.change_adopcion')
def modificarSol(request, id):
    
    solicitud = get_object_or_404(Adopcion, id=id)

    data={
        'form': AdopcionAdminForm(instance=solicitud)
    }
    if request.method=='POST':
        formulario=AdopcionAdminForm(data=request.POST, instance=solicitud)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="list_adopcion")
        data["form"]=formulario

    return render(request, "tablas/modificarsol.html", data)

@permission_required('albergue.delete_adopcion')
def eliminar_solicitud(request, id):
    solicitud = get_object_or_404(Adopcion, id=id)
    solicitud.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="list_adopcion")


class ListaMascotasView(ListView):
    model = Mascota
    template_name = "albergue/mascotas.html"
    context_object_name = 'mascotas'

class ListaMascotasPdf(View):

    def get(self, request, *args, **kwargs):
        mascotas = Mascota.objects.all()
        data = {

            'mascotas' : mascotas
        }
        pdf = render_to_pdf('albergue/lista_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
