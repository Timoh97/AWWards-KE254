
from django.urls import path
from . import views



urlpatterns = [
path('',views.index, name='index'),
path('profile/',views.profile, name='profile'),
path('accounts/profile/', views.profile, name='profile'),
path('upload/project/', views.upload, name = "upload"),
path('update_profile/<int:id>',views.update_profile, name='update_profile'),
path('create_profile/',views.create_profile,name = 'create_profile'),
# path('search/', views.search_projects, name='search'),
path('search/', views.search_results, name='search_results'),
path('rate/<int:id>',views.rate, name='rate'),
path("project/<int:project_id>/", views.project_details, name="project_details"),
# setting API endpoint
path('api/projects/', views.ProjectList.as_view()),
path('api/profiles/',views.ProfileList.as_view())
]
