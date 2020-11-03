from django.db import models


class ProjectCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Project categories'

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Skill categories'

    def __str__(self):
        return self.name

