from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Project
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import MerchSerializer
from rest_framework import status
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

class  ProjectList(APIView):
    def get(self, request, format=None):
        all_merch = Project.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)
    def post(self,request,format=None):
        serializers = MerchSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)