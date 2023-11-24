import json

from channels.generic.websocket import AsyncWebsocketConsumer


class QueueConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.queue_name = self.scope['url_route']['kwargs']['filial_slug']
        self.queue_group_name = f'queue_s'

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.discard(self.queue_group_name, self.channel_name)

    # async def receive(self, text_data=None, bytes_data=None):
    #     text_data = json.loads(text_data)
    #     ticket = TicketSerializer(text_data['ticket'])
    #
    #     await self.channel_layer.group_send(self.queue_group_name,
    #                                         {'type'})
    async def add_ticket_to_queue(self, event):
        ticket = event['ticket']
        print('===============================================')
        print(event['type'])
        print(ticket)
        print('===============================================')
        await self.send(text_data=json.dumps(ticket))
