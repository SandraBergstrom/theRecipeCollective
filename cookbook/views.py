# Based on the "Python Django Tutorial: Full-Featured Web App" tutorial by Corey Schafer
# Tutorial: https://youtu.be/UmljXZIypDc
# Snippet adapted from the tutorial with modifications

from django.shortcuts import render, redirect
from .models import Recipe
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

def index(request):
    if request.user.is_authenticated:
        return redirect ('cookbook-home')
    else:
        return render(request, 'index.html')

# this class will list all recipes with the latest
# recipe listed first
class RecipeListView(ListView):
    model = Recipe
    template_name = 'cookbook/home.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']
    paginate_by = 9

    def get_queryset(self):
        return Recipe.objects.filter(status=1)


# this class will show the recipe with all details.
class RecipeDetailView(DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        user = self.request.user
        if user.is_authenticated:
            if recipe.favorites.filter(id=user.id).exists():
                context['favorite'] = True
            else:
                context['favorite'] = False
        return context

# This class will make it possible to create a new recipe
class RecipeCreateView(LoginRequiredMixin, CreateView):
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

    # If the form is valid it will first check if user is logged in and if so
    # the user will be set as the author. If not it will redirect to the login page.
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            return super().form_valid(form)
        else:
            return self.form.invalid(form)


# this class will update the recipe
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    # If the form is valid it will first check if user is logged in and if so
    # the user will be set as the author. If not it will redirect to the login page.
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            return super().form_valid(form)
        else:
            return self.form.invalid(form)

    # will check if the logged in user is the author and if so, allow
    # them to update the recipe
    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False


# this class will delete the recipe
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = '/'

    # will check if the logged in user is the author and if so, allow
    # them to delete the recipe
    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False

# Shows the about page 
class AboutView(TemplateView):
    template_name = 'cookbook/about.html'
    extra_content = {'title': 'About'}

    