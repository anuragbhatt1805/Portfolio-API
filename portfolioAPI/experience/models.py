from django.db import models
from certification.models import Language

# Create your models here.
class Experience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    remote = models.BooleanField(default=False)
    location = models.CharField(max_length=100)
    description = models.TextField()
    tech = models.ManyToManyField(Language)
    start_date = models.DateField()
    end_date = models.DateField()
    objects = models.Manager()