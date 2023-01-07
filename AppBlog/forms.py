from django import forms



class AutorForm(forms.Form):
    nombre = forms.CharField (max_length = 80, label='Nombre Autor' )
    apellido = forms.CharField (max_length = 80, label='Apellido' )
    edad= forms.IntegerField (label='Edad')
    correo = forms.EmailField (max_length= 100, label='Correo')
    ubicacion = forms.CharField (max_length = 200, label='Ubicacion geografica')
    descripcion = forms.CharField (label='Descripcion')

class ArticuloForm (forms.Form):
    titulo = forms.CharField (max_length = 200, label='Nombre Articulo')
    subtitulo = forms.CharField (max_length = 200, label='Subtitulo del Articulo')
    cuerpo = forms.CharField (label = 'Contenido del Articulo')
    fecha_publicacion = forms.DateField (label='Fecha de Publicacion')
    