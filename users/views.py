from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from cookbook.models import Recipe

# registtration view for new user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, 
                f'Welcome { username }! Your account was successfully created! Please log in!'
                )
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# view for profile page
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(
                request, 
                f'Your account has been successfully updated!'
                )
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
        
    }
    return render(request, 'users/profile.html', context)


# view to filter favorite field to see if user id is there or not. If 
# the user id is there the user can remove from its favorites. If the 
# user id isn't there the user can add to favorites.
@login_required
def favorite_add(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if recipe.favorites.filter(id=request.user.id).exists():
        recipe.favorites.remove(request.user)
    else:
        recipe.favorites.add(request.user)
    # redirect to the current page
    return redirect(request.META.get('HTTP_REFERER'))


# view for the users list of favorites
@login_required
def favorite_list(request):
    new = Recipe.favorite_objects.get_queryset(user=request.user)
    return render(request, 'users/favorites.html', {'new': new})