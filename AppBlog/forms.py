from django import forms
from .models import *


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellido', 'edad', 'correo', 'ubicacion', 'descripcion'] #llenar todos los campos que tiene el modelo

class ArticuloForm (forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha_publicacion'] #'imagen']