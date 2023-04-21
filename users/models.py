from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='/static/users/profile_pics/default.jpg', upload_to='profile_pics')
    food_relation_choices = [
        ('CHEF', 'Chef'),
        ('NUTRITIONIST', 'Nutritionist'),
        ('PASTRY_CHEF', 'Pastry Chef'),
        ('FOOD_STYLIST', 'Food Stylist'),
        ('CULINARY_INSTRUCTOR', 'Culinary Instructor'),
        ('FOOD_CRITIC', 'Food Critic'),
        ('HOME_COOK', 'Home Cook'),
        ('OTHER', 'Other'),
    ]
    food_relation = models.CharField(max_length=30, choices=food_relation_choices, default='HOME_COOK')

    def __str__(self):
        return f'{self.user.username} Profile'

