
from django.urls import path
from . import views



urlpatterns = [
path('',views.index, name='index'),
path('profile/',views.profile, name='profile'),
path('accounts/profile/', views.profile, name='profile'),
path('upload/project/', views.upload, name = "upload"),
path('update_profile/<int:id>',views.update_profile, name='update_profile'),
path('create_profile/',views.create_profile,name = 'create_profile'),

]
