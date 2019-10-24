from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Project
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import MerchSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
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
            title=form.cleaned_data['title']
            image=form.cleaned_data['image']
            description=form.cleaned_data['description']
            link=form.cleaned_data['link']
             
            saveProfile = Profile(title=title,image=image,description=description,link=link,)
            saveProfile.save()
            return redirect('profile')
    else:
        form = UpdateForm()
        return render(request,'profile.html',{'form':form})

class  ProjectList(APIView):
    def get(self, request, format=None):
        all_merch = Project.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        permission_classes = (IsAdminOrReadOnly,)
        return Response(serializers.data)
    def post(self,request,format=None):
        serializers = MerchSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch)
        return Response(serializers.data)