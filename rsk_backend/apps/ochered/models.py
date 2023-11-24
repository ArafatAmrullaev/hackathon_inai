from django.db import models

from apps.customers.models import Customer
from apps.filial.models import Kassa

class Operation(models.Model):
    name = models.CharField()
    weight = models.IntegerField()


class Ticket(models.Model):
    customer = models.ForeignKey(Customer, related_name='tickets', on_delete=models.CASCADE)
    kassa = models.ForeignKey(Kassa, related_name='tickets', on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, related_name='tickets', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    appointment_start = models.DateTimeField(null=True)
    serviced_at = models.DateTimeField(null=True)
    