# from django.shortcuts import render
from rest_framework import viewsets
from project.models import Project
from project.serializer import ProjectSerializer


# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer