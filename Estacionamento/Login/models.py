from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    numero = models.CharField(max_length=16)
    sexo =  models.CharField(max_length=50)
    aniversario = models.DateField()
    placacar = models.CharField(max_length=50)
    car = models.CharField(max_length=50)