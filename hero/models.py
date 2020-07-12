from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=(('Male', 'M'), ('Female', 'F')), default='Female')
    movie = models.CharField(max_length=100)