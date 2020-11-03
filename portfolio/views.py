from django.http import FileResponse, Http404
from django.shortcuts import render
from .models import Certification, Skill, Project
from users.models import CustomUser as User


def index(request):
    bio = User.objects.get(id=1)
    skills = Skill.objects.order_by('name')
    context = {'bio': bio, 'skills': skills}
    return render(request, 'portfolio/index.html', context)


def certifications(request):
    certifications = Certification.objects.order_by('-date_completed')
    context = {'certifications': certifications}
    return render(request, 'portfolio/certifications.html', context)


def certification(request, certification_id):
    try:
        certification = Certification.objects.get(id=certification_id)
        file = str(certification.file)
        return FileResponse(open(file, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()


def projects(request):
    projects = Project.objects.order_by('date_completed')
    context = {'projects': projects}
    return render(request, 'portfolio/projects.html', context)


def project(request, project_id):
    project = Project.objects.get(id=project_id)
    context = {'project': project}
    return render(request, 'portfolio/project.html', context)


def skill(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    context = {'skill': skill}
    return render(request, 'portfolio/skill.html', context)
