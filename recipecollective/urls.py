from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('cookbook.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('favorites/<int:id>/', user_views.favorite_add, name='favorite_add'),
    path('favorites/', user_views.favorite_list, name='favorite_list'),
    path('myrecipes/', user_views.my_recipe_list, name='myrecipes'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
