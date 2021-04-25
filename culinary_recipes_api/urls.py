from django.urls import path
from .views import RecipeList, RecipeDetail, IngredientDetail, IngredientList

app_name = 'culinary_recipes_api'

urlpatterns = [
    path('<rec_id>/', RecipeDetail.as_view()),
    path('', RecipeList.as_view()),
    path('ingredients/', IngredientList.as_view()),
    path('ingredients/<ing_id>/', IngredientDetail.as_view()),
]