import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models
from django.forms.models import model_to_dict

from apps.customers.models import Customer
from apps.filial.models import Kassa



class Operation(models.Model):
    letter = models.CharField(max_length=1)
    name = models.CharField(max_length=255)
    weight = models.IntegerField()


class Ticket(models.Model):
    customer = models.ForeignKey(Customer, related_name='tickets', on_delete=models.CASCADE, null=True)
    kassa = models.ForeignKey(Kassa, related_name='tickets', on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, related_name='tickets', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    appointment_start = models.DateTimeField(null=True)
    serviced_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'queue_s',
            {
                'type': 'add.ticket.to.queue',
                'ticket': json.dumps(self.id)
            }
        )

    def __str__(self):
        return f'{self.operation.letter}{self.pk}'
