from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.
def Inicio (request):
    return render (request,'AppBlog/inicio.html')

def autores (request):
    return render (request, 'AppBlog/autores.html')

def articulos (request):
    return render (request, 'AppBlog/articulos.html')

def crear_articulo (request):
    if request.method == "POST":
        form=ArticuloForm (request.POST)

        if form.is_valid():
            informacionart=form.cleaned_data    
            titulo= informacionart['titulo']
            subtitulo= informacionart ['subtitulo']
            cuerpo= informacionart ['cuerpo']
            autorart= informacionart ['autorart']
            #fecha_publicacion = informacionart ['publicacion']
            imagen=informacionart ['imagen']
            articulocreado= Articulo(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autorart, imagen=imagen)
            articulocreado.save()
            articulos=Articulo.objects.all()
            return render(request, "AppBlog/articulos.html", {"articulos": articulos, "mensaje": "Articulo Creado Correctamente"})
        

        else:
            return render (request, 'AppBlog/crear_articulo.html', {"form": form, "mensaje": "Informacion no valida"} )

    else:
        formularioart=ArticuloForm()
        return render (request, 'AppBlog/crear_articulo.html', {'form': formularioart})



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
            URL= informacion ['URL']
            retrato= informacion ['retrato']
            autorcito= Autor (nombre=nombre, apellido=apellido, edad=edad, correo=correo, ubicacion=ubicacion, descripcion=descripcion, URL= URL, retrato=retrato)
            autorcito.save()
            autores= Autor.objects.all()
            return render (request, 'AppBlog/autores.html', {"autores": autores, "mensaje": "Autor Creado Correctamente"})
        
        else:
            return render(request,'AppBlog/crear_autor.html', {"form": form, "mensaje": "Informacion no valida"} )

    else:
        formulario= AutorForm()
        return render (request, 'AppBlog/crear_autor.html', {'form': formulario})

def usuario (request):
    return render (request,'AppBlog/crear_usuario.html')


def busquedatitulo (request):
    return render (request, 'AppBlog/busquedatitulo.html')

def buscar(request):
    
    titulo= request.GET["titulo"]
    if titulo!="":
        titulos= Articulo.objects.filter(titulo__icontains=titulo)
        return render(request, "AppBlog/resultadosbusqueda.html", {"titulo": titulos})
    else:
        return render(request, "AppBlog/busquedatitulo.html", {"mensaje": "Ingresar un Titulo para buscar"})

#def leerautores(request):
    #autores=Autor.objects.all()
    #return render (request, 'AppBlog/Autores.html', {'Autores': autores})