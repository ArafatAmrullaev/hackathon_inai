from rest_framework import serializers

from .models import Address, Filial, Kassa

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = '__all__'


class KassaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kassa
        fields = '__all__'