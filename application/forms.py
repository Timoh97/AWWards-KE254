from .models import Profile, Project
from django.forms import ModelForm
from django import forms


class PostProjectForm (ModelForm):
    class Meta:
        model=Project
        fields = (
            'image',
            'description',
            'category',
            'location',
            'url',
            'name'   
        )
        
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo','contact')
        
        
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        filed = ('bio', 'profile_photo','contact')