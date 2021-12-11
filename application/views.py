from django.shortcuts import render, redirect
from django.http  import HttpResponse
from . models import Profile, Project
from . forms import UpdateProfileForm
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    
    return render(request, 'index.html')


def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id).first()
    return render(request,"profile.html",{'profile':profile,'project':project})


def user_project(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request,"profile.html",{'profile':profile})


def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():      
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile' ,username=user.username) 
            
    ctx = {"form":form}
    return render(request, 'update_profile.html',{"form":form})