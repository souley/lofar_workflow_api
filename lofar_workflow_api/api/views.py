from django.shortcuts import render
from django.http import JsonResponse, Http404
from rest_framework import generics, permissions
from .serializers import *#SessionSerializer
from .models import *#Session
from .permissions import IsOwner


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# PUT THIS ON FOR AUTHENTICATION!!
authentication_on = False

# Create your views here.

##
# Sessions
class CreateSessionsView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data_dict = dict(request.data.dict())
        data_dict.update({"status":"started"})

        serializer = SessionSerializer(data=data_dict)#request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CreateSessionsView(generics.ListCreateAPIView):
#     """This class defines the create behaviour of our rest api"""
#     queryset = Session.objects.all()
#     serializer_class = SessionSerializer
    
#     # if authentication_on:
#     #   permission_classes = (permissions.IsAuthenticated, IsOwner)

#     def perform_create(self, serializer):
#        # print( self.get_queryset() )
#         #serializer.is_valid()
#         serializer.save()#owner=self.request.user)

#         """ Now start the pipeline """
#         #new_session = Session.objects.get(pk=serializer.data["id"])
#         ## START THE PIPELINE HERE
#         # ....
#         # ....
#         #pipeline_output = "Hij is goed gestart :)"
#         #pipeline_started = True
#         ##
#         #new_session.pipeline_respone = pipeline_output
#         #if pipeline_started:
#         #    new_session.status = "started"
#         #new_session.save()

#         #return JsonResponse(new_session.data)

#         """Save the post data when creating a new Session"""
#         #serializer.save()#owner=self.request.user)



class SessionDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This handles the http GET, PUT and DELETE requests"""

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    # if authentication_on:
    #   permission_classes= (permissions.IsAuthenticated, IsOwner)

# ##
# # PipelineConfigurations
# class CreatePipelineConfigurationsView(generics.ListCreateAPIView):
#   """This class defines the create behaviour of our rest api"""
#   queryset = PipelineConfiguration.objects.all()
#   serializer_class = PipelineConfigurationSerializer
    
#   # if authentication_on:
#   #   permission_classes = (permissions.IsAuthenticated, IsOwner)

#   def perform_create(self, serializer):
#       """Save the post data when creating a new Session"""
#       serializer.save()#owner=self.request.user)

# class PipelineConfigurationDetailsView(generics.RetrieveUpdateDestroyAPIView):
#   """This handles the http GET, PUT and DELETE requests"""

#   queryset = PipelineConfiguration.objects.all()
#   serializer_class = PipelineConfigurationSerializer
#   # if authentication_on:
#   #   permission_classes= (permissions.IsAuthenticated, IsOwner)


# ##
# # ObservationData
# class CreateObservationsView(generics.ListCreateAPIView):
#   """This class defines the create behaviour of our rest api"""
#   queryset = Observation.objects.all()
#   serializer_class = ObservationSerializer
    
#   # if authentication_on:
#   #   permission_classes = (permissions.IsAuthenticated, IsOwner)

#   def perform_create(self, serializer):
#       """Save the post data when creating a new Session"""
#       serializer.save()#owner=self.request.user)

# class ObservationDetailsView(generics.RetrieveUpdateDestroyAPIView):
#   """This handles the http GET, PUT and DELETE requests"""

#   queryset = Observation.objects.all()
#   serializer_class = ObservationSerializer
#   # if authentication_on:
#   #   permission_classes= (permissions.IsAuthenticated, IsOwner)

