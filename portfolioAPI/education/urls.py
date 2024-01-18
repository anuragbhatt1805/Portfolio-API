from django.urls import path, include
from education.views import EducationViewSet, AchievementViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('education', EducationViewSet)
router.register('achievement', AchievementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]