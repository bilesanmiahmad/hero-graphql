from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', blank=True)
    in_stock = models.BooleanField(default=True)
    date_created = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name