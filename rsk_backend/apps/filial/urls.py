from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import AddressViewSet, FilialViewSet, KassaViewSet

router = DefaultRouter()
router.register('address', AddressViewSet)
router.register('kassa', KassaViewSet)
router.register('', FilialViewSet)

urlpatterns = [
    path('', include(router.urls))
]