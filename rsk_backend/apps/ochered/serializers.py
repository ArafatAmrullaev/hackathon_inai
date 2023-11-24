from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import serializers

from .models import Operation, Ticket

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        channel_layer = get_channel_layer()
        serialized = self.to_representation(instance=instance)
        async_to_sync(channel_layer.group_send)(
            f'queue_{instance.kassa.filial.slug}',
            {
                'type': 'add.ticket',
                'ticket': serialized
            }
        )
        async_to_sync(channel_layer.group_send)(
            f'kassa_{instance.kassa.slug}',
            {
                'type': 'send_ticket',
                'ticket': serialized
            }
        )
        return instance
