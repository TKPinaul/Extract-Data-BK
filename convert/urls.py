from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SomeViewSet  # Remplacez `SomeViewSet` par vos propres vues

# Créer un routeur pour gérer les vues
router = DefaultRouter()
router.register(r'some-endpoint', SomeViewSet)  # Remplacez `some-endpoint` et `SomeViewSet` selon vos besoins

urlpatterns = [
    path('', include(router.urls)),  # Inclut toutes les routes du routeur
]