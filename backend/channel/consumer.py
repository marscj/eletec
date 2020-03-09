from rest_framework import views, response

from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer

from asgiref.sync import async_to_sync
import json

class MessageConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
            
        await self.accept()

        await self.channel_layer.group_add("message", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("message", self.channel_name)

    async def send_message(self, event):
        await self.send_json({"msg_type": 0, "message": event["message"]})


        