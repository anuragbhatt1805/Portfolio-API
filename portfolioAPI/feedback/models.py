from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    title = models.CharField(max_length=100)
    feedback = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()