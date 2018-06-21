from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *# CreateSessionsView, SessionDetailsView

urlpatterns = {
	url(r'^auth/', include('rest_framework.urls',
                               namespace='rest_framework')), 
	url(r'^sessions/$', CreateSessionsView.as_view(), name="create"),
	url(r'^sessions/(?P<pk>[0-9]+)/$', SessionDetailsView.as_view(), name='details'),
	# url(r'^pipelineconfigurations/$', CreatePipelineConfigurationsView.as_view(), name="create"),
	# url(r'^pipelineconfigurations/(?P<pk>[0-9]+)/$', PipelineConfigurationDetailsView.as_view(), name='details'),
	# url(r'^observations/$', CreateObservationsView.as_view(), name="create"),
	# url(r'^observations/(?P<pk>[0-9]+)/$', ObservationDetailsView.as_view(), name='details'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
#print(urlpatterns)