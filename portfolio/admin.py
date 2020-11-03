from django.forms import TextInput, Textarea
from django.db import models
from django.contrib import admin
from .models import Certification, Project, Skill


class CertificationDisplay(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 40, 'cols': 70})},
    }
    fields = ('id', 'title', 'date_completed', 'file')
    list_display = ('title',)


class ProjectDisplay(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 40, 'cols': 70})},
    }
    fields = ('id', 'name', ('category', 'work_in_progress'), ('cover_image', 'dark_cover_image'), 'description', 'date_completed')
    list_display = ('name', 'category', 'work_in_progress')
    list_filter = ('category', 'work_in_progress')


class SkillDisplay(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 40, 'cols': 70})},
    }
    list_display = ('name', 'category')
    list_filter = ('category', )


admin.site.register(Certification, CertificationDisplay)
admin.site.register(Project, ProjectDisplay)
admin.site.register(Skill, SkillDisplay)
