from django.db import models


# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=64)

class Dish(models.Model):
    name = models.CharField(max_length=64)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=False)

class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    dishes = models.ManyToManyField(Dish)
