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
            if command == 'order':
                await self.channel_layer.group_send('message', {'type': 'order.message', 'message': content['message'], 'pk': content['pk']})
            elif command == 'job':
                await self.channel_layer.group_send('message', {'type': 'job.message', 'message': content['message'], 'pk': content['pk']})
            elif command == 'comment':
                await self.channel_layer.group_send('message', {'type': 'comment.message', 'message': content['message'], 'pk': content['pk']})

        except ClientError as e:
            # Catch any errors and send it back
            await self.send_json({'error': e.code})

    async def order_message(self, event):
        await self.send_json({'msg_type': 0, 'messageID': str(uuid.uuid1()), 'message': event['message'], 'pk': event['pk'], 'date': str(timezone.localtime())})

    async def job_message(self, event):
        await self.send_json({'msg_type': 1, 'messageID': str(uuid.uuid1()), 'message': event['message'], 'pk': event['pk'], 'date': str(timezone.localtime())})

    async def comment_message(self, event):
        await self.send_json({'msg_type': 2, 'messageID': str(uuid.uuid1()), 'message': event['message'], 'pk': event['pk'], 'date': str(timezone.localtime())})


        