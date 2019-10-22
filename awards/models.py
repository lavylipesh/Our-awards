from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='images/')
    bio = models.TextField(default="")

    def __str__(self):
        return f'{self.user.username}Profile'

class Update(models.Model):
    bio = models.TextField(default = "")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bio')
    
    def __str__(self):
        return self.bio

