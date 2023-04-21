from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Private"), (1, "Public"))

class Recipe(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    excerp = models.CharField(max_length=50, blank=True, null=True)
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
