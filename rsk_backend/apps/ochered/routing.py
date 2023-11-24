from django.urls import re_path

from .consumers import QueueConsumer, KassaConsumer

websocket_urlpatterns = [
    re_path(r'ws/queue/(?P<kassa_id>[\w-]+)/$', QueueConsumer.as_asgi()),
    re_path(r'ws/kassa/(?P<kassa_id>[\w-]+)/$', KassaConsumer.as_asgi()),
]
