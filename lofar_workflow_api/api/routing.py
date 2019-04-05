# api/routing.py
from django.urls import path
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
#    path('ws/api//', consumers.JobStateConsumer),
    url(r'^ws/api/(?P<jobid>[-\w]+)/$', consumers.JobStateConsumer),
]
