from django.urls import path, include
from project.views import ProjectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('project', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]