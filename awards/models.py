from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='images/')
    bio = models.TextField(default="")

    def __str__(self):
        return f'{self.user.username}Profile'

#class Update(models.Model):
    #bio = models.TextField(default = "")
    #user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bio')
    #profile_pic = models.ImageField(default='default.jpg', upload_to='images/')
    
    #def __str__(self):
        #return self.bio
        
class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='images/',blank=True)
    link = models.CharField(max_length=100)
   
 


