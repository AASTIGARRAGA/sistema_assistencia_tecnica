from django.db import models

# Create your models here.
class Pecas(models.Model):
    nome=models.CharField(max_length=100)
    codigo=models.IntegerField()
    preço=models.IntegerField()


    