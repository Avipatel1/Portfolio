from django.shortcuts import render, redirect
from .models import Project, Report

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

# for scientific reports
def scientific_reports(request):
    reports = Report.objects.all()
    return render(request, 'main/reports.html', {
        'reports': reports,
    })