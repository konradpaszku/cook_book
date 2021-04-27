from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField(max_length=1000)
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.title
