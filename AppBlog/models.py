from django.db import models

# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField (max_length = 80, blank = False, null = False)
    apellido = models.CharField (max_length = 80, blank = False, null = False)
    edad= models.IntegerField (null = True, blank = True)
    correo = models.EmailField (unique = True, max_length= 100)
    ubicacion = models.CharField (max_length = 200, blank = False, null = False)
    descripcion = models.TextField (blank = False, null = False)
    #instagram = models.URLField ()
    #retrato = models.ImageField()

    def __str__(self):
        return f'{self.nombre} { self.apellido}'


