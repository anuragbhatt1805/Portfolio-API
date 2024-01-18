# from django.shortcuts import render
from rest_framework import viewsets
from users.models import AdminData
from users.serializer import DataSerializer
from users.permission import UpdateOwnProfile


class DataViewSet(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    queryset = AdminData.objects.all()
    permission_classes = (UpdateOwnProfile,)

