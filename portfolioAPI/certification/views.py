# from django.shortcuts import render
from rest_framework import viewsets
from certification.models import Certification, Badges, Language
from certification.serializer import (
    CertificationSerializer,
    BadgesSerializer,
    LanguageSerializer
)


# Create your views here.
class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class BadgesViewSet(viewsets.ModelViewSet):
    queryset = Badges.objects.all()
    serializer_class = BadgesSerializer