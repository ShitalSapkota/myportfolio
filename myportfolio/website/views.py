from django.shortcuts import render, redirect
from .models import *


def index(request):
    abouts = About.objects.all()
    certificates = Certificate.objects.all()
    images = Image.objects.all()
    skills = Skill.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    resumes = ResumeList.objects.all()
    return render(request,'home/home.html', {'abouts': abouts,
                                             'certificates': certificates,
                                             'images': images,
                                             'skills': skills,
                                             'educations': educations,
                                             'experiences': experiences})


# def about_page(request):
#     about = About.objects.all()
#     return render(request, 'sidebar/about.html', {'about': about})

