from django.urls import path

from . import views

app_name = 'culinary_recipes'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    path('/ingredients', views.ingredients, name='ingredients'),
    path('/recipe/<rec_id>/', views.recipe, name='recipe'),
]