from django.urls import path, include
from users.views import DataViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', DataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]