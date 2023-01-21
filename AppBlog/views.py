from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
def Inicio (request):
    return render (request,'AppBlog/inicio.html')

def autores (request):
    return render (request, 'AppBlog/autores.html')

def articulos (request):
    return render (request, 'AppBlog/articulos.html')


#------------------------------ Crear Articulo ------------------------------------ 

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

#--------------------------------- Crear Autor ----------------------------------------------------

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

#-----------------------------------Busqueda titulo------------------------------------------------------------------------------


def busquedatitulo (request):
    return render (request, 'AppBlog/busquedatitulo.html')




#def buscar(request):
    
#    titulo= request.GET["titulo"]
#    if titulo!="":
#        articulos= Articulo.objects.filter(titulo__icontains=titulo)
 #       return render(request, "AppBlog/resultadosbusqueda.html", {"articulos": articulos})
 #   else:
 #       return render(request, "AppBlog/busquedatitulo.html", {"mensaje": "Ingresar un Titulo para buscar"})
        

#---------------------------leer / eliminar / editar autor--------------------------------------------------------------


def leerautores(request):
    autores=Autor.objects.all()
    return render (request, 'AppBlog/Autores.html', {'autores': autores})

def eliminarautor (request, id):
    autor= Autor.objects.get(id=id)
    print (autor)
    autor.delete()
    autores= Autor.objects.all ()
    return render (request, 'AppBlog/autores.html', {'autores': autores, "mensaje": "Autor eliminado correctamente"})

def editarautor (request,id):
    autor=Autor.objects.get(id=id)
    if request.method=="POST":
        form= AutorForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            autor.nombre= informacion['nombre']
            autor.apellido= informacion ['apellido']
            autor.edad= informacion ['edad']
            autor.correo=informacion['correo']
            autor.ubicacion=informacion['ubicacion']
            autor.descripcion= informacion ['descripcion']
            autor.URL= informacion ['URL']
            autor.retrato= informacion ['retrato']
            autor.save()
            autor= Autor.objects.all()
            return render (request, 'AppBlog/autores.html', {"autores": autores, "mensaje": "Autor Editado Correctamente"})
        pass
        
    else:
        formulario= AutorForm(initial={"Nombre":autor.nombre, "Apellido":autor.apellido, "Edad":autor.edad, "profesion":autor.correo, "ubicacion":autor.ubicacion, "descripcion": autor.descripcion })
        return render (request, 'AppBlog/crear_autor.html', {'form': formulario})



#-------------------------------leer / eliminar / editar  articulo---------------------------------------------------------------------------------


def leerarticulos(request):
    articulos=Articulo.objects.all()
    return render (request, 'AppBlog/Articulos.html', {'articulos': articulos})

def eliminarticulo(request, id):
    articulo= Articulo.objects.get(id=id)
    print (articulo)
    articulo.delete()
    articulos= Articulo.objects.all ()
    return render (request, 'AppBlog/articulos.html', {'articulos': articulos, "mensaje": "Articulo eliminado correctamente"})

def editararticulo (request,id):
    articulo=Articulo.objects.get(id=id)
    if request.method=="POST":
        form= ArticuloForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            Articulo.titulo= informacion['titulo']
            Articulo.subtitulo= informacion ['subtitulo']
            Articulo.cuerpo= informacion ['cuerpo']
            Articulo.autor=informacion['autor']
            Articulo.fecha_entrega=informacion['fecha_entrega']
            Articulo.imagen= informacion ['imagen']
            articulo.save()
            articulos= Articulo.objects.all()
            return render (request, 'AppBlog/articulos.html', {"articulos": articulos, "mensaje": "Articulo Editado Correctamente"})
        pass
        
    else:
        formulario= AutorForm(initial={"titulo": articulo.titulo, "subtitulo":articulo.subtitulo, "cuerpo":articulo.cuerpo, "autor":articulo.autor, "fecha_entrega":articulo.fecha_entrega, "imagen": articulo.imagen })
        return render (request, 'AppBlog/crear_articulo.html', {'form': formulario})


#------------------------- Boton borrar Autor --------------------------------------------------------------------------------------


class autorList(LoginRequiredMixin, ListView):
    model= Autor
    template_name= "AppCoder/autores.html"

class autorCreacion(LoginRequiredMixin,CreateView):
    model= Autor
    success_url= reverse_lazy("autor_list")
    fields=['nombre', 'apellido','edad', 'email']

class autorUpdate(LoginRequiredMixin,UpdateView):
    model= Autor
    success_url = reverse_lazy('autor_list')
    fields=['nombre', 'apellido','edad', 'email']


class autorDelete(LoginRequiredMixin,DeleteView):#vista usada para ELIMINAR
    model= Autor
    success_url = reverse_lazy('autor_list')


#------------------------- Boton borrar articulo --------------------------------------------------------------------------------------


class articuloList(LoginRequiredMixin, ListView):
    model= Articulo
    template_name= "AppCoder/articulos.html"

class articuloCreacion(LoginRequiredMixin,CreateView):
    model= Articulo
    success_url= reverse_lazy("articulo_list")
    fields=['nombre', 'apellido','edad', 'email']

class articuloUpdate(LoginRequiredMixin,UpdateView):
    model= Articulo
    success_url = reverse_lazy('articulo_list')
    fields=['nombre', 'apellido','edad', 'email']


class articuloDelete(LoginRequiredMixin,DeleteView):#vista usada para ELIMINAR
    model= Articulo
    success_url = reverse_lazy('articulo_list')