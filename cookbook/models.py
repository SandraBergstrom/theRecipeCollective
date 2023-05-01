from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


# Status for user to set if recipe should be public or private
STATUS = ((0, "Private"), (1, "Public"))

"""
Model that represents a recipe that users can create, view, update and delete.
Includes fields for title, author, featured image, excerpt, about, category, preparation
and cooking time, servings, ingredients, instructions, date posted, date updated and status
"""
class Recipe(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField(
        'image', 
        default='https://res.cloudinary.com/sandrabergstrom/image/upload/v1682690083/placeholder_got9h5.jpg'
        )
    excerp = models.CharField(max_length=200, blank=True, null=True)
    about = models.TextField(max_length=600, blank=True, null=True)
    category_choices = [
        ('APPETIZERS', 'Appetizers'),
        ('BREAKFAST', 'Breakfast'),
        ('MAIN_DISHES', 'Main Dishes'),
        ('DESSERTS', 'Desserts'),
        ('SALLADS', 'Sallads'),
        ('SIDE_DISHES', 'Side Dishes'),
        ('SNACKS', 'Snacks'),
        ('OTHER', 'Other'),
    ]
    category = models.CharField(max_length=30, choices=category_choices, default="MAIN_DISHES")
    prep_time = models.DurationField(blank=True, null=True)
    cooking_time = models.DurationField(blank=True, null=True)
    servings = models.IntegerField(default=1) 
    ingredients = models.TextField()
    instructions = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

    # Will show the user the recipe-detail page for the recipe posted
    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})