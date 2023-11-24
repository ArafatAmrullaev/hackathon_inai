from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import OperationViewSet, TicketViewSet, queue

router = DefaultRouter()
router.register('operation', OperationViewSet)
router.register('ticket', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('queue_online/<str:queue_name>/', queue)
]