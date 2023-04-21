# Generated by Django 3.2.18 on 2023-04-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_food_relation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='food_relation',
            field=models.CharField(choices=[('CHEF', 'Chef'), ('NUTRITIONIST', 'Nutritionist'), ('PASTRY_CHEF', 'Pastry Chef'), ('FOOD_STYLIST', 'Food Stylist'), ('CULINARY_INSTRUCTOR', 'Culinary Instructor'), ('FOOD_CRITIC', 'Food Critic'), ('HOME_COOK', 'Home Cook'), ('OTHER', 'Other')], default='HOME_COOK', max_length=30),
        ),
    ]