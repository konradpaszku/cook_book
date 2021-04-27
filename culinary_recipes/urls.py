from django.urls import path

from . import views

app_name = 'culinary_recipes'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #list of ingredients
    path('ingredients', views.ingredients, name='ingredients'),
    #one recipe
    path('recipe/<rec_id>/', views.recipe, name='recipe'),
    #sorted recipes
    path('sortrecipes/', views.index_sort, name='index_sort'),
]