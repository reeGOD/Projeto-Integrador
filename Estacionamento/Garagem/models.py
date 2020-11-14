from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Garagem(models.Model):
    iduser = models.IntegerField()
    validacao=models.BooleanField()
    
class vagas(models.Model):
    iduser = models.IntegerField()
    validacao=models.BooleanField()
    
class vagass(models.Model):
    iduser = models.IntegerField()
    validacao=models.BooleanField()