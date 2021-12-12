from django.shortcuts import render, redirect
from django.http  import HttpResponse
from . models import Profile, Project
from . forms import UpdateProfileForm,ProfileForm, PostProjectForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse,HttpResponseRedirect

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id).first()
    return render(request,"profile.html",{'profile':profile,'project':project})

@login_required(login_url='/accounts/login/')
def user_project(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request,"profile.html",{'profile':profile})

@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    ctx = {"form":form}
    return render(request, 'update_profile.html', ctx)


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form, "title": title})


@login_required(login_url='/accounts/login/')
def upload(request):
    if request.method == "POST":
        form = PostProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
        return redirect('/')
    else:
        form = PostProjectForm()
    return render(request, 'project.html', {"form": form})