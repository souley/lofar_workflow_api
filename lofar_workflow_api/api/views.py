from django.shortcuts import render
from django.http import JsonResponse, Http404, QueryDict
from rest_framework import generics, permissions
from .serializers import *
from .models import *
from .permissions import IsOwner

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# This handles the available pipelines
from .pipeline_administrator import get_available_pipelines

# Put this on for authentications
authentication_on = False

##
# Sessions
class CreateSessionsView(APIView):

    # This function checks if the given pipeline name and config are
    # valid
    def check_pipeline_config(self, pipeline, config):
        if pipeline in get_available_pipelines().keys():
            if list(config.keys()) == get_available_pipelines()[pipeline].give_argument_names():
                return True
            else:
                return False
        else:
            return False

    def get(self, request, format=None):
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = SessionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            id_session = serializer.data["id"]
            
            current_session = Session.objects.get(pk=id_session)
            
            pipeline_configured = self.check_pipeline_config(current_session.pipeline, current_session.config)
            if pipeline_configured:

                ## The pipeline is executed here
                current_session.pipeline_respone = \
                    get_available_pipelines()[current_session.pipeline].run_pipeline(**current_session.config)

                current_session.pipeline_version = get_available_pipelines()[current_session.pipeline].give_version()
                current_session.status = "started"
                current_session.save()
                new_ser = SessionSerializer(current_session)
                return Response(new_ser.data, status=status.HTTP_201_CREATED)
            else:
                current_session.delete()
                return Response("Pipeline unknown or pipeline wrongly configured. Nothing was done", \
                                status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class SessionDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This handles the http GET, PUT and DELETE requests"""

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    # if authentication_on:
    #   permission_classes= (permissions.IsAuthenticated, IsOwner)
