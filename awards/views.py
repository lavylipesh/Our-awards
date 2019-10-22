from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Project
#from .forms import UpdateForm

@login_required(login_url='/accounts/login/')
def index(request):
    images = Project.objects.all()
    return render(request,'index.html',{'images':images})
   
def profile(request):
    current_user=request.user   
    profile=Profile.objects.filter(id=current_user.id)
    return render(request,'profile.html',{'profile':profile})

@login_required(login_url='/accounts/login/')
def update(request):
    
    if request.method == 'POST':
        form = UpdateForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            saveProfile = Profile(profile_pic=profile_pic)
            saveProfile.save()
            return redirect('profile')
    else:
        form = UpdateForm()
        return render(request,'profile.html',{'form':form})

