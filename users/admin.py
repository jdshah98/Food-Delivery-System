from django.contrib import admin
from .models import Profile, UserType

# Register your models here.
admin.site.register(UserType)
admin.site.register(Profile)