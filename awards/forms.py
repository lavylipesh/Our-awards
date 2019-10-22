from django.forms import ModelForm
from .models import *

    
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields=['user','profile_pic']

class UpdateForm(ModelForm):
    class Meta:
        model = Update
        fields = ['update']