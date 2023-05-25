from django.contrib import admin

# Register your models here.

from myapp.models import UserProfile
admin.site.register(UserProfile)
