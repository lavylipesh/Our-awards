from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'index.html')
   
def profile(request):
    current_user=request.user   
    image=Image.objects.filter(profile_id=current_user.id)
    return render(request,'profile.html',{'image':image})