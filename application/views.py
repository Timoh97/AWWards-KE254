from django.shortcuts import render
from django.http  import HttpResponse
from . models import Profile
# Create your views here.

def index(request):
    
    return render(request, 'index.html')


def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request,"profile.html",{'profile':profile})