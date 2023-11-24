from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Operation, Ticket
from .serializers import OperationSerializer, TicketSerializer


class OperationViewSet(ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


def queue(request, queue_name):
    return render(request, "ochered/queue.html", {"queue_name": queue_name})
