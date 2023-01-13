from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def Inicio (request):
    return render (request,'AppBlog/inicio.html')

def autores (request):
    return render (request, 'AppBlog/autores.html')

def articulos (request):
    return render (request, 'AppBlog/articulos.html')

def creararticulo (request):
    if request.method == 'POST':
        form=ArticuloForm (request.POST)
        if form.is_valid():
            informacionart=form.cleaned_data
            titulo= informacionart['titulo']
            subtitulo= informacionart ['subtitulo']
            cuerpo= informacionart ['cuerpo']
            autor= informacionart ['autor']
            publicacion= informacionart ['publicacion']
            articulocreado= Articulo(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, publicacion=publicacion)
            articulocreado.save()
            articulos=Articulo.objects.all()
            return render(request, "AppBlog/articulos.html", {"articulos": articulos, "mensaje": "Articulo Creado Correctamente"})
        

        else:
            return render (request, 'AppBlog/crear_articulo.html', {"form": form, "mensaje": "Informacion no valida"} )

    else:
        formularioart=ArticuloForm
        return render (request, 'AppBlog/crear_articulo.html', {'fromart': formularioart})



def crearautor (request):
    if request.method=='POST':
        form= AutorForm (request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion['nombre']
            apellido= informacion ['apellido']
            edad= informacion ['edad']
            correo=informacion['correo']
            ubicacion=informacion['ubicacion']
            descripcion= informacion ['descripcion']
            autorcito= Autor (nombre=nombre, apellido=apellido, edad=edad, correo=correo, ubicacion=ubicacion, descripcion=descripcion)
            autorcito.save()
            autores= Autor.objects.all()
            return render (request, 'AppBlog/autores.html', {"autores": autores, "mensaje": "Autor Creado Correctamente"})
        
        else:
            return render(request,'AppBlog/crear_autor.html', {"form": form, "mensaje": "Informacion no valida"} )

    else:
        formulario= AutorForm
        return render (request, 'AppBlog/crear_autor.html', {'form': formulario})

def usuario (request):
    return render (request,'AppBlog/crear_usuario.html')