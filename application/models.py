from django.db import models

# Create your models here.

from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# profile of the user.
class Profile(models.Model):
  profile_photo= CloudinaryField('image')
  bio = models.TextField()
  contact = models.CharField(max_length=30)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  # save profile method
  def save_profile(self):
    self.save()
    
  # Save profile method
  def delete_profile(self):
    self.delete()
  
  def __str__(self):
    return self.bio




class Project(models.Model):
  image = CloudinaryField('image')
  name = models.TextField(max_length=30)
  description = models.TextField()
  location = models.TextField()
  category = models.TextField()
  url = models.URLField(blank=True)
  date_posted = models.DateTimeField(auto_now=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
  
  
  # Save image method
  def save_project(self):
    self.save()
    
  # Get all images method
  @classmethod
  def get_all_project(cls):
    all_project=cls.objects.all()
    return all_project
  
  def __str__(self):
    return self.name
  
# class Like(models.Model):
#   like=models.IntegerField()
#   project = models.ForeignKey(Project, on_delete=models.CASCADE, default='DEFAULT VALUE')
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
  
#   def __str__(self):
#     return self.like
  
  
# class Comment(models.Model):
#   comment_message = models.TextField()
#   posted_on = models.DateTimeField(auto_now=True)
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   project = models.ForeignKey(Project, on_delete=models.CASCADE, default='DEFAULT VALUE')
  
#   def __str__(self):
#     return self.user.username