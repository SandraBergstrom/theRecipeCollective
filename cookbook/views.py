from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView, DetailView, CreateView



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


class RecipeCreateView(CreateView):
    model = Recipe
    fields = [
        'title', 
        'excerp', 
        'featured_image', 
        'category', 
        'prep_time', 
        'cooking_time',
        'servings',
        'ingredients',
        'instructions',
        'instructions',
        'status',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'cookbook/about.html', {'title': 'About'})