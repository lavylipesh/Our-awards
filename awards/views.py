from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Project,CommentForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import MerchSerializer
from .forms import ProjectForm,UpdateForm,MyCommentForm

@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.objects.all()
    form = MyCommentForm()
    comment = CommentForm.objects.all()

    return render(request,'index.html',{'MyCommentForm':form,'projects':projects})
   
def profile(request):
    current_user=request.user   
    profile=Profile.objects.filter(id=current_user.id)
    return render(request,'profile.html',{'profile':profile})

@login_required(login_url='/accounts/login/')
def update(request,format=None):
    if request.method == 'POST':
        form = UpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():      
            form.save()            
            return redirect('profile')
    else:
        form = UpdateForm(instance=request.user.profile)
    return render(request,'update.html',{'form':form})

class  ProjectList(APIView):
    def get(self, request, format=None):
        all_merch = Project.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)
    

@login_required(login_url='/accounts/login/')
def upload(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            link = form.cleaned_data['link']
            image = form.cleaned_data['image']
            user = request.user
            saveProject = Project(title=title,description=description,link=link,image=image,user=user)
            saveProject.save_project()
            return redirect('index')
    else:
        form = ProjectForm()
    return render(request,'project.html',{'form':form})


def comment(request,pk):
    
    if request.method == 'POST':
        form = MyCommentForm(request.POST)
        if form.is_valid():
            image = Image.objects.get(pk=pk)
            user = request.user
            comment = form.save(commit=False)
            comment.image = image
            comment.user = user
            comment.save()
            return redirect('index')
    else:
        print("error")
        return redirect('index')

def review(request):
    pass