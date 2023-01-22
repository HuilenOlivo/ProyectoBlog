from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="/media/avatars/avatarpordefecto.png"
    return avatar


def Inicio (request):
    return render (request,'AppBlog/inicio.html')

@login_required
def autores (request):
    return render (request, 'AppBlog/autores.html', { "avatar": obtenerAvatar(request)})

@login_required
def articulos (request):
    return render (request, 'AppBlog/articulos.html', { "avatar": obtenerAvatar(request)})


#------------------------------ Crear Articulo ------------------------------------ 
@login_required
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
            return render(request, "AppBlog/articulos.html", {"articulos": articulos, "mensaje": "Articulo Creado Correctamente"}, { "avatar": obtenerAvatar(request)})
        

        else:
            return render (request, 'AppBlog/crear_articulo.html', {"form": form, "mensaje": "Informacion no valida"})

    else:
        formularioart=ArticuloForm()
        return render (request, 'AppBlog/crear_articulo.html', {'form': formularioart})

#--------------------------------- Crear Autor ----------------------------------------------------
@login_required
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
            return render (request, 'AppBlog/autores.html', {"autores": autores, "mensaje": "Autor Creado Correctamente"}, { "avatar": obtenerAvatar(request)})
        
        else:
            return render(request,'AppBlog/crear_autor.html', {"form": form, "mensaje": "Informacion no valida"})

    else:
        formulario= AutorForm()
        return render (request, 'AppBlog/crear_autor.html', {'form': formulario})

def usuario (request):
    return render (request,'AppBlog/crear_usuario.html')

#-----------------------------------Busqueda titulo------------------------------------------------------------------------------

@login_required
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

@login_required
def leerautores(request):
    autores=Autor.objects.all()
    return render (request, 'AppBlog/Autores.html', {'autores': autores}, { "avatar": obtenerAvatar(request)})

@login_required
def eliminarautor (request, id):
    autor= Autor.objects.get(id=id)
    print (autor)
    autor.delete()
    autores= Autor.objects.all ()
    return render (request, 'AppBlog/autores.html', {'autores': autores, "mensaje": "Autor eliminado correctamente"}, { "avatar": obtenerAvatar(request)})

@login_required
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

@login_required
def leerarticulos(request):
    articulos=Articulo.objects.all()
    return render (request, 'AppBlog/Articulos.html', {'articulos': articulos})

@login_required
def eliminarticulo(request, id):
    articulo= Articulo.objects.get(id=id)
    print (articulo)
    articulo.delete()
    articulos= Articulo.objects.all ()
    return render (request, 'AppBlog/articulos.html', {'articulos': articulos, "mensaje": "Articulo eliminado correctamente"})

@login_required
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



#------------------------- Registro Usuario---------------------------   
def registro (request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "AppBlog/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppBlog/registro.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "AppBlog/registro.html", {"form": form})


#------------------------- Ingresar Usuario---------------------------  
def ingresar_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)#verifica si el usuario existe, si existe, lo devuelve, y si no devuelve None 
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppBlog/inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "AppBlog/ingresar.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppBlog/ingresar.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "AppBlog/ingresar.html", {"form": form})


#------------------------- Editar Perfil --------------------------- 
@login_required 
def editarperfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]            
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]

            usuario.save()
            return render(request, "AppBlog/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "AppBlog/editarperfil.html", {"form": form, "nombreusuario":usuario.username})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppBlog/editarperfil.html", {"form": form, "nombreusuario":usuario.username})


#------------------------- Crear Avatar ---------------------------  
def agregaravatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppBlog/inicio.html", {"mensaje":f"Avatar agregado correctamente"})
        else:
            return render(request, "AppBlog/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "AppBlog/agregarAvatar.html", {"form": form, "usuario": request.user})



