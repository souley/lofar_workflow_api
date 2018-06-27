from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls',
                               namespace='rest_framework')), 
    url(r'^sessions$', CreateSessionsView.as_view(), name="create"),
    url(r'^sessions/$', CreateSessionsView.as_view(), name="create"),
    url(r'^sessions/(?P<pk>[0-9]+)/$', SessionDetailsView.as_view(), name='details'),
}

urlpatterns = format_suffix_patterns(urlpatterns)