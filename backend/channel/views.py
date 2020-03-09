from rest_framework import views, response

from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer

from asgiref.sync import async_to_sync
import json

class MessageConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        
        # if self.scope["user"].is_anonymous:
        #     await self.close()
        # else:
            
        await self.accept()

        await self.channel_layer.group_add("chat", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("chat", self.channel_name)

    async def chat_message(self, event):
        print(event)
        await self.send_json({"msg_type": 0, "message": event["message"]})


        