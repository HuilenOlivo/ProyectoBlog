from django.shortcuts import render
from .models import *
from AppBlog.forms import *


# Create your views here.
def Inicio (request):
    return render (request,'AppBlog/inicio.html')

def autores (request):
    return render (request, 'AppBlog/autores.html')

def articulos (request):
    return render (request, 'AppBlog/articulos.html')

def crear_articulo (request):
    if request.method == 'POST':
        tituloarticulo= request.POST ['titulo_articulo']
        subtituloarticulo= request.POST ['subtitulo_articulo']
        cuerpoarticulo= request.POST ['cuerpo_articulo']
        autorarticulo= request.POST ['autor_id']
        publicacionarticulo= request.POST ['publicacion_articulo']
        articulocreado= Articulo(tituloarticulo=tituloarticulo, subtituloarticulo=subtituloarticulo, cuerpoarticulo=cuerpoarticulo, autorarticulo=autorarticulo, publicacionarticulo=publicacionarticulo)
        articulocreado.save()
        return render(request, "AppBlog/articulos.html", {'mensaje': 'Articulo Guardado'})
    

    else:
        return render (request, 'AppBlog/crear_articulo.html')


'''def crearAutor (request):
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
        return render (request, 'AppBlog/crear_autor.html', {'form': formulario}) '''


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
