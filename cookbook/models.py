from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    excerp = models.CharField(max_length=50, blank=True, null=True)
    prep_time = models.DurationField(blank=True, null=True)
    cooking_time = models.DurationField(blank=True, null=True)
    servings = models.IntegerField(default=1) 
    ingredients = models.TextField()
    instructions = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

