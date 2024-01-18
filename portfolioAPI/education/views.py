# from django.shortcuts import render
from rest_framework import viewsets
from education.models import Education, Achievement
from education.serializer import EducationSerializer, AchievementSerializer


# Create your views here.
class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer