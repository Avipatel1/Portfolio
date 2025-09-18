from django.shortcuts import render, redirect
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {
        'projects': projects,
    })

