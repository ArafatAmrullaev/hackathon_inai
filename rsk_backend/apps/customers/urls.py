from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import CustomerViewSet

router = DefaultRouter()
router.register('', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls))
]