from django.shortcuts import render
from .models import *

# Create your views here.
def Inicio (request):
    return render (request,'AppBlog/index.html')

def autores (request):
    return render (request, 'AppBlog/autores.html')

def crearAutor (request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)

        if autor_form.is_valid():
            informacion=autor_form.cleaned_data
            nombre = informacion ['nombre']
            apellido = informacion ['apellido']
            edad = informacion ['edad']
            correo = informacion ['correo']  
            ubicacion = informacion ['ubicacion'] 
            descripcion = informacion ['descripcion']
            autorcito = Autor (nombre=nombre, apellido=apellido, edad=edad, correo=correo, ubicacion=ubicacion, descripcion=descripcion)
            autorcito.save()
            autores= Autor.objects.all()
            return render (request, 'AppBlog/autores.html', {"autores":autores, "mensaje": "Autor guardado correctamente"})
         
        else:
            return render (request, 'AppBlog/crear_autor.html',  {'autor_form': autor_form, 'mensaje': 'Informacion no valida'})

    else:
        formulario = AutorForm()
        return render (request, 'AppBlog/crear_autor.html', {'form': formulario}) 

          