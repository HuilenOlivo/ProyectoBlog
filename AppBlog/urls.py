from django.urls import path
from .views import *



urlpatterns = [

    path ('', Inicio, name = 'inicio'),
    path ('autores/', autores, name = 'autores'),
    path ('crear_autor/', crearautor, name = 'crear_autor'),
    path ('articulos/', articulos, name='articulos'),
    path ('crear_articulo/', crear_articulo, name= 'crear_articulo'),    
    path ('crear_usuario/', usuario, name= 'crear_usuario'),

##------------------- Busqueda titulo --------------------        
    #path ('busquedatitulo/', busquedatitulo, name= 'busquedatitulo'),
    #path ('buscar/', buscar, name= buscar),

#------------------- leer / eliminar / editar --------------------    
    #path ('leerautores/', leerautores, name=leerautores),
    #path ('eliminarautor/<id>', eliminarautor, name=eliminarautor),
    #path ('editarautor/<id>', editarautor , name=editarautor),

    #path ('leerarticulos/', leerarticulos, name=leerautores),
    #path ('eliminararticulos/', eliminarautor, name=eliminarautor),
    #path ('editararticulos/', editarautor, name=editarautor),

#------------------- Borrar Autor --------------------    
    path ('autor/list/', autorList.as_view(), name='autor_list'),
    path ('autor/borrar/<pk>', autorDelete.as_view(), name= 'autor_borrar'),


#------------------- Borrar Articulo --------------------    
    path ('articulo/list/', articuloList.as_view(), name='articulo_list'),
    path ('articulo/borrar/<pk>', articuloDelete.as_view(), name= 'articulo_borrar')
]