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

from . import views
import json
import requests

from .consumers import jobState
import tempfile
from PIL import Image

from django.conf import settings

from rest_framework.renderers import TemplateHTMLRenderer

# Put this on for authentications
authentication_on = False
initState = ''

class PipelineSchemasView(APIView):
    def get(self, request, format=None):
        response_dict = {}
        for p in get_available_pipelines():
            response_dict.update( get_available_pipelines()[p].give_config() )
        serializer = PipelinesSerializer({"pipelineschemas":response_dict})
        return Response(serializer.data)

##
# Sessions
class CreateSessionsView(APIView):

    # This function checks if the given pipeline name and config are
    # valid
    def check_pipeline_config(self, pipeline, config):

        if pipeline in get_available_pipelines().keys():
            if set(config.keys()) == set(get_available_pipelines()[pipeline].give_argument_names()):
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
                pipeline_res = \
                    get_available_pipelines()[current_session.pipeline].run_pipeline(current_session.observation, **current_session.config)
                
                print('===Session data from api.views.py')
                print(pipeline_res.content)
                res_data = json.loads(pipeline_res.content.decode("utf8"))
                current_session.pipeline_response = res_data['id']
                current_session.pipeline_version = get_available_pipelines()[current_session.pipeline].give_version()
                current_session.status = res_data['state']
#                current_session.status = "started"
                current_session.save()
#                res_data = json.loads(current_session.pipeline_response.content.decode("utf8"))
#                global initState
#                initState = res_data['state']
#                print('===api.views initState=', initState)
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

class SessionDetails(APIView):
    """
        Retrieve, update or delete a session instance.
        """
    def get_object(self, request, pk):
        session = None
        try:
            session = Session.objects.get(pk=pk)
#            return Session.objects.get(pk=pk)
        except Session.DoesNotExist:
            raise Http404
        # Update status from Xenon-flow server
        print('=SessionDetails::get_object() pp res: ', session.pipeline_response)
        url = 'http://localhost:8443/jobs/' + session.pipeline_response
        headers = {
            'Content-Type': 'application/json',
            'api-key': 'in1uP28Y1Et9YGp95VLYzhm5Jgd5M1r0CKI7326RHwbVcHGa'
        }
        data = {}
        res = requests.get(url, headers=headers, data=json.dumps(data))
#        print(res.content)
        res_data = json.loads(res.content.decode("utf8"))
        session.status = res_data['state']
        
#        image_name = settings.MEDIA_ROOT + '/P23wsclean_' + str(session.id) + '.jpg'
#        files = {'di_image': open(image_name, 'rb'),}
#        res = requests.put(request.build_absolute_uri() + 'di_image', files=files) # Method not allowed

#        if session.status == 'Success':
#        with tempfile.NamedTemporaryFile(suffix='.jpg') as fp:
#            image = Image.new('RGB', (100, 200))
#            image.save(fp)
#            fp.seek(0)
##            session.di_image =  list(image.getdata())
#            session.di_image =  fp

        session.save()
        return session


    def get(self, request, pk, format=None):
        session = self.get_object(request, pk)
        serializer = SessionSerializer(session)
        return Response(serializer.data)

#    def put(self, request, pk, format=None):
#        session = self.get_object(pk)
#        serializer = SessionSerializer(session, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        session = self.get_object(request, pk)
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SessionView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api/session_detail.html'

    """
        Retrieve, update or delete a session instance.
    """
    def get_object(self, pk):
        session = None
        try:
            session = Session.objects.get(pk=pk)
        except Session.DoesNotExist:
            raise Http404
        # Update status from Xenon-flow server
        print('=SessionDetails::get_object() pp res: ', session.pipeline_response)
        url = 'http://localhost:8443/jobs/' + session.pipeline_response
        headers = {
            'Content-Type': 'application/json',
            'api-key': 'in1uP28Y1Et9YGp95VLYzhm5Jgd5M1r0CKI7326RHwbVcHGa'
        }
        data = {}
        res = requests.get(url, headers=headers, data=json.dumps(data))
        #        print(res.content)
        res_data = json.loads(res.content.decode("utf8"))
        session.status = res_data['state']

        session.save()
        return session


    def get(self, request, pk, format=None):
        session = self.get_object(pk)
        serializer = SessionSerializer(session)
        return Response({'serializer': serializer, 'session': session})

    
def job(request, jobid):
#    print('===views.job request.data: ', request)
    global initState
    print('===views.job initState: ', initState, '\t,jobState: ', jobState)
    jobStatus = initState
    if jobStatus != jobState:
        jobStatus = jobState
    return render(request, 'api/job.html', {
                  'jobid': jobid,
                  'jobState': jobStatus
#                  'jobid': mark_safe(json.dumps(request.data))
                  })

class ImageDetails(APIView):
    def get(self, request, pk, format=None):
        session = self.get_object(request, pk)
        serializer = SessionSerializer(session)
        return Response(serializer.data['di_image'])
