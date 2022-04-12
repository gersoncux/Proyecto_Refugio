from cProfile import label
import email
from django import forms


class FormularioContacto(forms.Form):


    nombre=forms.CharField(label="Nombre", required=True)
    email=forms.EmailField(label="Email", required=True)
    mensaje=forms.CharField(label="contenido", widget=forms.Textarea)


    #asunto=forms.CharField()
    #email=forms.EmailField()
    #mensaje=forms.CharField()