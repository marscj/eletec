from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer

from asgiref.sync import async_to_sync
import json

from .exceptions import ClientError

class MessageConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
            
        await self.accept()

        await self.channel_layer.group_add("message", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("message", self.channel_name)

    async def receive_json(self, content):
        command = content.get("command", None)
        try:
            if command == "send":
                await self.channel_layer.group_send("message", {"type": "send.message", "message": content["message"]})
        except ClientError as e:
            # Catch any errors and send it back
            await self.send_json({"error": e.code})

    async def send_message(self, event):
        await self.send_json({"msg_type": 0, "message": event["message"]})


        