from django.urls import re_path

from .consumers import QueueConsumer

websocket_urlpatterns = [
    re_path('ws/queue/(?P<filial_slug>\w+)/$', QueueConsumer.as_asgi())
]
