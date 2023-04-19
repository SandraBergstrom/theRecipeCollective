from django.shortcuts import render

recipes = [
    {
        'author': 'CoreyMS',
        'title': 'Recipe 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Recipe 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'recipes': recipes
    }
    return render(request, 'cookbook/home.html', context)

def about(request):
    return render(request, 'cookbook/about.html', {'title': 'About'})