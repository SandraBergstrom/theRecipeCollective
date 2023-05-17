from django.contrib import admin
from .models import Profile, Comment

admin.site.register(Comment)
admin.site.register(Profile)
