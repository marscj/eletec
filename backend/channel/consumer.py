from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer
from django.utils import timezone

from asgiref.sync import async_to_sync
import json
import uuid

from .exceptions import ClientError

class MessageConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
            
        await self.accept()

        await self.channel_layer.group_add('message', self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('message', self.channel_name)

    async def receive_json(self, content):
        command = content.get('command', None)
        try:
            if command == 'send':
                await self.channel_layer.group_send('message', {'type': 'send.message', 'message': content['message'], 'objectID': content['objectID']})
        except ClientError as e:
            # Catch any errors and send it back
            await self.send_json({'error': e.code})

    async def send_message(self, event):
        await self.send_json({'msg_type': 0, 'messageID': str(uuid.uuid1()), 'message': event['message'], 'objectID':event['objectID'], 'read': False, 'date': str(timezone.localtime())})


        