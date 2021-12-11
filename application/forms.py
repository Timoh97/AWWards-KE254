from .models import Profile, Project
from django.forms import ModelForm
from django import forms


class PostProjectForm (ModelForm):
    class Meta:
        model=project
        fields = (
            'image',
            'description',
            'category',
            'location',
            'url',
            'name'   
        )