from django.shortcuts import render
from django.http import JsonResponse, Http404, QueryDict
from rest_framework import generics, permissions
from .serializers import *#SessionSerializer
from .models import *#Session
from .permissions import IsOwner


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .pipeline_administrator import get_available_pipelines
# PUT THIS ON FOR AUTHENTICATION!!
authentication_on = False


# Create your views here.

##
# Sessions
class CreateSessionsView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def check_pipeline_config(self, pipeline, config):

        print (get_available_pipelines())

        implemented_pipelines = {"LGPPP": ["avg_freq_step", "avg_time_step", "do_demix", "demix_freq_step", "demix_time_step", "demix_sources", "select_NL","parset"],\
                    }

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

        serializer = SessionSerializer(data=request.data)# (data=data_dict

        #if serializer.is_valid():
        if serializer.is_valid():
            print("Request", request.data)
            serializer.save()#status="started")
            id_session = serializer.data["id"]
            
            current_session = Session.objects.get(pk=id_session)
            
            ##
            ## START THE PIPELINE HERE
            ##
            pipeline_configured = self.check_pipeline_config(current_session.pipeline, current_session.config)
            if pipeline_configured:

                ## HERE IS THE MAGIC!
                current_session.pipeline_respone = get_available_pipelines()[current_session.pipeline].run_pipeline(**current_session.config)
                ##
                current_session.status = "started"
                current_session.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)#serializer.data,
            else:
                current_session.status = "failure"
                current_session.pipeline_respone = "Pipeline unknown or pipeline wrongly configured. Nothing was done"
                current_session.save()
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST) #
            
            #serializer.data["status"]="unknown"

            #print(current_session.pipeline)
            #print(current_session.config)
            ##
            ##
            ##

            

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CreateSessionsView(generics.ListCreateAPIView):
#     """This class defines the create behaviour of our rest api"""
#     queryset = Session.objects.all()
#     serializer_class = SessionSerializer
    
#     # if authentication_on:
#     #   permission_classes = (permissions.IsAuthenticated, IsOwner)

#     def perform_create(self, serializer):


#         """ Now start the pipeline """
#         #new_session = Session.objects.get(pk=serializer.data["id"])
#         ## START THE PIPELINE HERE
#         print(self.request.data)
#         print(serializer.validated_data)
#         #avg_freq_step = self.request.data["avg_freq_step"]
#         # ....
#         # ....
#         #pipeline_output = "Hij is goed gestart :)"
#         #pipeline_started = True
#         ##
#         #new_session.pipeline_respone = pipeline_output
#         #if pipeline_started:
#         #    new_session.status = "started"
#         #new_session.save()

#         """Save the post data when creating a new Session"""
#         #if serializer.is_valid():
#         serializer.save(status="started")#owner=self.request.user)



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

