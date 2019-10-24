from django.forms import ModelForm
from .models import *

class UpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user','profile_pic','bio']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields=['title','editor','description','link','image']