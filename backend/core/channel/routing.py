from django.urls import path

from . import consumer

websocket_urlpatterns = [
    path('notify/', consumer.MessageConsumer)
]