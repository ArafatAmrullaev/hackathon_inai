from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import OperationViewSet, TicketViewSet

router = DefaultRouter()
router.register('operation', OperationViewSet)
router.register('ticket', TicketViewSet)

urlpatterns = [
    path('', include(router.urls))
]