from django.urls import path
from .views import *



urlpatterns = [

    path ('', Inicio, name = 'inicio'),
    path ('autores/', autores, name = 'autores'),
    path ('crear_autor/', crearautor, name = 'crear_autor'),
    path ('articulos/', articulos, name='articulos'),
    path ('crear_articulo/', crear_articulo, name= 'crear_articulo'),    
   


]