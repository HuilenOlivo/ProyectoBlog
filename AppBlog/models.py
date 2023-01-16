from django.db import models

# Create your models here.
class CreadorBlog (models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField (max_length = 80, blank = False, null = False, verbose_name= 'Nombre')
    apellido = models.CharField (max_length = 80, blank = False, null = False, verbose_name = 'Apellido' )
    edad= models.IntegerField (null = True, blank = True, verbose_name = 'Edad')
    correo = models.EmailField (unique = True, max_length= 100, verbose_name = 'Correo')
    descripcion = models.TextField (blank = False, null = False, verbose_name = 'Descripcion')


    def __str__(self):
        return f'{self.nombre} - { self.apellido}'


class Autor (models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField (max_length = 80, blank = False, null = False, verbose_name= 'Nombre')
    apellido = models.CharField (max_length = 80, blank = False, null = False, verbose_name = 'Apellido' )
    edad= models.IntegerField (null = True, blank = True, verbose_name = 'Edad')
    correo = models.EmailField (unique = True, max_length= 100, verbose_name = 'Correo')
    ubicacion = models.CharField (max_length = 200, blank = False, null = False, verbose_name = 'ubicacion')
    descripcion = models.TextField (blank = False, null = False, verbose_name = 'Descripcion')
    #URL = models.URLField (blank=True, verbose_name = 'URL')
    #retrato =  models.ImageField(blank=True, upload_to= 'AppBlog/imagenes')    


    def __str__(self):
        return f'{self.nombre} - { self.apellido}'


class Articulo (models.Model):
    id = models.AutoField(primary_key= True)
    titulo = models.CharField (max_length = 200, blank = True, null = False, verbose_name = 'titulo')
    subtitulo = models.CharField (max_length = 200, blank = True, null = False, verbose_name = 'subtitulo')
    cuerpo = models.TextField (blank = False, null = True, verbose_name = 'cuerpo')
    autor = models.CharField (max_length=200, verbose_name = 'autor', null= True) #Si se borra el articulo, tambien al autor que se relaciona
    #fecha_entrega= models.DateField()
    imagen= models.ImageField(blank=True, upload_to= 'AppBlog/imagenes')    
    

    def __str__(self):
        return f'{self.titulo}'
        
        
class usuario (models.Model):
    nombre= models.CharField (max_length = 200, blank = False, null = False, verbose_name = 'usuario')