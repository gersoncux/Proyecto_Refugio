from attr import field
from django import forms
from matplotlib import widgets
from RefugiowebApp.models import Datos
from .models import Mascota, Adopcion

class DatosForm(forms.ModelForm):

    class Meta:
        model=Datos
        fields='__all__'

class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = '__all__'

class MascotaAddForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = ["nombre","categorias","imagen","alimentacion","vacunas","raza","sexo_mascota"]

class AdopcionForm(forms.ModelForm):

    class Meta:
        model = Adopcion
        fields = ["nombre","telefono","direccion","email","nombre_mascota"]


class AdopcionAdminForm(forms.ModelForm):

    class Meta:
        model = Adopcion
        fields = ["nombre","telefono","direccion","email","nombre_mascota", "estado"]

# Si hay que ingresar fechas desde un form, se puede utilizar el widgets dentro del meta
'''
class MascotaForm(forms.ModelForm):
    
    class Meta:
        model = Mascota
        fields = '__all__'

        widgets = {
            "fecha": forms.SelectDateWidget
        }
'''