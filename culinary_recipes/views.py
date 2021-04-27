from django.shortcuts import render
from .models import Ingredient, Recipe


def index(request):
    """Home page"""
    recipes = Recipe.objects.order_by('id')
    context = {'recipes': recipes}
    return render(request, 'culinary_recipes/index.html', context)


def ingredients(request):
    """Show list of ingredients"""
    ingredients = Ingredient.objects.order_by('id')
    context = {'ingredients': ingredients}
    return render(request, 'culinary_recipes/ingredients.html', context)


def recipe(request, rec_id):
    """Show one recipe"""
    recipe = Recipe.objects.get(pk=rec_id)
    context = {'recipe': recipe}
    return render(request, 'culinary_recipes/recipe.html', context)


def index_sort(request):
    """Home page with sorted recipes"""
    recipes = Recipe.objects.order_by('title')
    context = {'recipes': recipes}
    return render(request, 'culinary_recipes/index.html', context)
