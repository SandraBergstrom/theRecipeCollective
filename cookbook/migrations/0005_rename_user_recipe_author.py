# Generated by Django 3.2.18 on 2023-04-21 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0004_rename_author_recipe_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='user',
            new_name='author',
        ),
    ]
