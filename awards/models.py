from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    name=models.CharField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='images/')
    bio = models.TextField(default="")

    def __str__(self):
        return f'{self.user.username}Profile'
        
class Project(models.Model):
    editor = models.CharField(max_length=60)
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='images/',blank=True)
    link = models.URLField(max_length=100)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'


    def save_project(self):
        self.save()
 

