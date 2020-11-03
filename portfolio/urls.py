from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('certifications/', views.certifications, name='certifications'),
    path('certifications/<certification_id>', views.certification, name='certification'),
    path('projects/', views.projects, name='projects'),
    path('projects/<project_id>', views.project, name='project'),
    path('skills/<skill_id>', views.skill, name='skill'),
]
