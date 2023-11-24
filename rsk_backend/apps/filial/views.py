from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import Address, Filial, Kassa
from .serializers import AddressSerializer, FilialSerializer, KassaSerializer

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class FilialViewSet(ModelViewSet):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer


class KassaViewSet(ModelViewSet):
    queryset = Kassa.objects.all()
    serializer_class = KassaSerializer

