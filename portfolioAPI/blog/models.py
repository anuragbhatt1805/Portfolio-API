from django.db import models
import os, uuid

# Create your models here.
def blogPic(instance, filepath):
    "Function for Profile Picture"
    ext = os.path.splitext(filepath)[1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join('blog', filename)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    picture = models.ImageField(upload_to=blogPic, null=True, blank=True)
    likes = models.IntegerField(default=0)
    objects = models.Manager()

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Anonymous")
    comment = models.TextField()
    objects = models.Manager()