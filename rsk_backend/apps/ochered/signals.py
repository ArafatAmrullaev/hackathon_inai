# import json
#
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync
# from .models import Ticket
# from .serializers import TicketSerializer
#
#
# @receiver(post_save, sender=Ticket)
# def post_ticket_saved_signal(sender, instance, created, **kwargs):
#     if created:
#         print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         'queue_semetei',
#         {
#             'type': 'add_ticket_to_queue',
#             'ticket': json.dumps(TicketSerializer(instance).data)
#         }
#     )
#
