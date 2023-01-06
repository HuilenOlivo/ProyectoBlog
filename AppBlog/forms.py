from django import forms



class AutorForm(forms.Form):
    nombre = forms.CharField (max_length = 80, blank = False, null = False, label='Nombre Autor' )
    apellido = forms.CharField (max_length = 80, blank = False, null = False, label='Apellido' )
    edad= forms.IntegerField (null = True, blank = True, label='Edad')
    correo = forms.EmailField (unique = True, max_length= 100, label='Correo')
    ubicacion = forms.CharField (max_length = 200, blank = False, null = False, label='Ubicacion geografica')
    descripcion = forms.TextField (blank = False, null = False, label='Descripcion')

class ArticuloForm (forms.Form):
    titulo = forms.CharField (max_length = 200, blank = False, null = False, label='Nombre Articulo')
    subtitulo = forms.CharField (max_length = 200, blank = False, null = False, label='Subtitulo del Articulo')
    cuerpo = forms.TextField (blank = False, null = False, verbose_name = 'Contenido del Articulo')
    fecha_publicacion = forms.DateField ('Fecha de publicacion', blank = False, null = False, label='Fecha de Publicacion')
    