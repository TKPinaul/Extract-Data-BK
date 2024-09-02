from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataFileViewSet

router = DefaultRouter()
router.register(r'data-files', DataFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]