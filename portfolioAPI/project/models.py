from django.db import models
from certification.models import Language
import uuid, os

def project(instance, filepath):
    ext = os.path.splitext(filepath)[1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join('image', 'project', filename)

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(Language)
    image = models.ImageField(upload_to=project, null=True)
    repsitory = models.URLField(max_length=200)
    url = models.URLField(max_length=200)
    objects = models.Manager()