from django.forms import ModelForm
from .models import *
from django import forms

class UpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','profile_pic','bio']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields=['title','editor','description','link','image']