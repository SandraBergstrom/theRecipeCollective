from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView, DetailView


def home(request):
    context = {
        'recipes': Recipe.objects.all(),
    }
    return render(request, 'cookbook/home.html', context)


class RecipeListView(ListView):
    model = Recipe
    template_name = 'cookbook/home.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']


class RecipeDetailView(DetailView):
    model = Recipe
    

def about(request):
    return render(request, 'cookbook/about.html', {'title': 'About'})