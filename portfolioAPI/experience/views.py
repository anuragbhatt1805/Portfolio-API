# from django.shortcuts import render
from rest_framework import viewsets
from experience.models import Experience
from experience.serializer import ExperienceSerializer


# Create your views here.
class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer