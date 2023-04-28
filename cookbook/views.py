from django.shortcuts import render
from .models import Recipe
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DetailView
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# def home(request):
#     context = {
#         'recipes': Recipe.objects.all(),
#     }
#     return render(request, 'cookbook/home.html', context)


# this class will list all recipes with the latest
# recipe listed first
class RecipeListView(ListView):
    model = Recipe
    template_name = 'cookbook/home.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']


# this class will show the recipe with all details.
class RecipeDetailView(DetailView):
    model = Recipe

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

    # will check if the logged in user is the author and if so, allow
    # them to delete the recipe
    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False




def about(request):
    return render(request, 'cookbook/about.html', {'title': 'About'})