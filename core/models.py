from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class TipoRopa(models.Model):

    ropa = models.CharField(max_length=80);

    def __str__(self):
        return self.ropa

class DescripcionRopa(models.Model):

    nombre = models.CharField(max_length=100)

    color =models.CharField(max_length=20)

    valor = models.CharField(max_length=50)    

    stock = models.IntegerField()

    talla = models.CharField(max_length=50)

    grupoRopa = models.ForeignKey(TipoRopa, on_delete=CASCADE) # fk para llevar la desc. al tipo de ropa

    def __str__(self):
        return self.nombre
    
    
    
    