from culinary_recipes.models import Recipe, Ingredient
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'context', 'ingredients')
        depth = 1
