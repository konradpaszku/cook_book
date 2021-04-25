from rest_framework import generics
from culinary_recipes.models import Recipe, Ingredient
from .serializers import IngredientSerializer, RecipeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetail(APIView):
    def get(self, request, ing_id):
        try:
            query = Ingredient.objects.get(pk=ing_id)
            serializer = IngredientSerializer(query)
            return Response(serializer.data, status=200)
        except Ingredient.DoesNotExist:
            return Response(None, status=400)


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetail(APIView):
    def get(self, request, rec_id):
        try:
            query = Recipe.objects.get(pk=rec_id)
            serializer = RecipeSerializer(query)
            return Response(serializer.data, status=200)
        except Recipe.DoesNotExist:
            return Response(None, status=400)