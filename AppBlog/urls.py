from django.urls import path
from .views import *



urlpatterns = [

    path ('', Inicio, name = 'index'),
    path ('crear_autor/', crearAutor, name = 'crear_autor'),
    path ('autores/', autores, name = 'autores')
   


]