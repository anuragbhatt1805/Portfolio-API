from django.urls import path, include
from certification.views import (
    LanguageViewSet,
    CertificationViewSet,
    BadgesViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('language', LanguageViewSet)
router.register('certification', CertificationViewSet)
router.register('badges', BadgesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]