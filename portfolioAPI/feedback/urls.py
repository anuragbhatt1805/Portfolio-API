from django.urls import path, include
from feedback.views import FeedbackViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]