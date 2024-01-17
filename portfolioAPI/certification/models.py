from django.db import models
import uuid, os

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=20)
    objects = models.Manager()

class Certification(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    certification_id = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    tags = models.ManyToManyField(Language)
    url = models.URLField(max_length=200)
    objects = models.Manager()

def badgepic(instance, filepath):
    ext = os.path.splitext(filepath)[1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join('image', 'badge', filename)

class Badges(models.Model):
    title = models.CharField(max_length=100)
    badge = models.ImageField(upload_to=badgepic, null=True)
    tags = models.ManyToManyField(Language)
    url = models.URLField(max_length=200)
    objects = models.Manager()