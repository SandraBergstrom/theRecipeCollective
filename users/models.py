from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from cookbook.models import Recipe



"""
Model that extends the user model and adds fields image,
food relation and country.
"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField(
        'image', 
        default='https://res.cloudinary.com/sandrabergstrom/image/upload/v1683716250/user_minu4x.png'
        )
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
    food_relation = models.CharField(
        max_length=30, 
        choices=food_relation_choices, 
        default='HOME_COOK'
        )
    country = models.CharField(
        max_length=200, 
        default='Citizen of the world'
        )

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}, {self.get_food_relation_display()}'


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"