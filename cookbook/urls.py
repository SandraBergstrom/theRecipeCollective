from django.urls import path
from . import views
from .views import (
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView
)

urlpatterns = [
    path('', RecipeListView.as_view(), name='cookbook-home'),
    path('about/', views.about, name='cookbook-about'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe-create'),
]