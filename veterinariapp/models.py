from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=500)

    def __str__(self):
        return self.nome 
    
class Animais(models.Model):
    nome = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=200, decimal_places= 2, default= 0)
    altura = models.DecimalField(max_digits=200, decimal_places= 2, default= 0)
    descrição = models.CharField(max_length=500)
    imagem = models.ImageField()
    categoria = models.ManyToManyField ( 'Categoria' , related_name = 'Animais' )

    def __str__(self):
        return self.nome 