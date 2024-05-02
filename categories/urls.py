from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='brand')

urlpatterns = [
    path('', include(router.urls)),
    # Add other app URLs here
]
