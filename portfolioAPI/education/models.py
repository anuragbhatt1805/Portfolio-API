from django.conf import settings
from django.db import models


# Create your models here
class Education(models.Model):
    institute = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    grade_style = models.CharField(max_length=255, choices=[("cgpa", "CGPA"), ("percentage", "PERCENTAGE")])
    grade = models.FloatField(null=True, blank=True)
    objects = models.Manager()


class Achievement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    objects = models.Manager()