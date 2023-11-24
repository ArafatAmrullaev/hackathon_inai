from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import Operation, Ticket
from .serializers import OperationSerializer, TicketSerializer

class OperationViewSet(ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
