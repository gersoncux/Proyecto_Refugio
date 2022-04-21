from django.contrib import admin
from RefugiowebApp.models import Datos
from .models import CategoriaMascota, Mascota, Sexo, Adopcion


class DatosAdmin(admin.ModelAdmin):
    list_display=("Nombre","Telefono","Direccion","Mascota","Ocupacion","Edad_de_mascota","Fecha")
    search_fields=("Nombre","Telefono")


class CategoriaMascotaAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

class MascotaAdmin(admin.ModelAdmin):
    list_display=("nombre","categorias","disponibilidad","raza","sexo_mascota")
    search_fields=("nombre","raza")
    readonly_fields=("created","updated")

class VacunaAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

class SexoAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

class SolicitudAdmin(admin.ModelAdmin):
    list_display=("nombre","telefono","direccion","email","nombre_mascota","estado")
    readonly_fields=("created","updated")




admin.site.register(Datos, DatosAdmin)

admin.site.register(CategoriaMascota, CategoriaMascotaAdmin)

admin.site.register(Mascota, MascotaAdmin)

admin.site.register(Sexo, SexoAdmin)

admin.site.register(Adopcion, SolicitudAdmin)
