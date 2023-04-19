from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cookbook-home'),
    path('about/', views.about, name='cookbook-about'),
]