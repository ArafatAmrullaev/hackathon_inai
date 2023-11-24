import json

from channels.generic.websocket import AsyncWebsocketConsumer


class QueueConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.queue_name = self.scope['url_route']['kwargs']['filial_slug']
        self.queue_group_name = f"queue_{self.queue_name}"

        await self.channel_layer.group_add(self.queue_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.queue_group_name, self.channel_name)

    async def add_ticket(self, event):
        ticket = event['ticket']
        await self.send(text_data=json.dumps({ticket}))


class KassaConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.kassa_name = self.scope['url_route']['kwargs']['kassa_id']
        self.kassa_group_name = f'kassa_{self.kassa_name}'

        await self.channel_layer.group_add(self.kassa_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.kassa_group_name, self.channel_name)

    async def send_ticket(self, event):
        ticket = event['ticket']
        await self.send(text_data=json.dumps(ticket))
