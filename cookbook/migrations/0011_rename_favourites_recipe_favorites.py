# Generated by Django 3.2.18 on 2023-05-03 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0010_recipe_favourites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='favourites',
            new_name='favorites',
        ),
    ]