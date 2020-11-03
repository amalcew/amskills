from django.db import models
from datetime import date
from django.core.validators import FileExtensionValidator
from dateutil.relativedelta import relativedelta
from pdf2image import convert_from_path
from django.dispatch import receiver
from categories.models import ProjectCategory, SkillCategory


class Certification(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=200)
    date_completed = models.DateField()
    file = models.FileField(upload_to='static/media', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    cover_image = models.ImageField(blank=True)

    def __str__(self):
        return self.title


@receiver(models.signals.post_save, sender=Certification)
def extract_cover(sender, instance, created, *args, **kwargs):
    if created:
        pdf = instance.file
        cover = convert_from_path(str(pdf), 100)
        cover = cover[0]
        cover_name = str(pdf)[12:-4]
        cover.save('static/images'+cover_name+".jpg", 'JPEG')

        instance.cover_image = 'static/images'+cover_name+".jpg"
        instance.save()


class Project(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    description = models.TextField()
    date_completed = models.DateField()
    work_in_progress = models.BooleanField(default=False)
    cover_image = models.ImageField(upload_to='static/images', blank=True)
    dark_cover_image = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    description = models.TextField()
    date_started = models.DateField()

    def get_time(self):
        difference = relativedelta(date.today(), self.date_started)
        years = difference.years
        months = difference.months
        if years != 0:
            if years == 1:
                if months >= 6:
                    return "year and a half"
                return "%s year" % years
            else:
                if months >= 6:
                    return "%s years and a half" % years
                return "%s years" % years
        elif months != 0:
            if months == 1:
                return "%s month" % months
            else:
                return "%s months" % months
        else:
            return "less than a month"

    def __str__(self):
        return self.name