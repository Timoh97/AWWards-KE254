from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import Project, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)