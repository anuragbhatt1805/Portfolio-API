from django.urls import path, include
from users.views import DataViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('anurag', DataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]