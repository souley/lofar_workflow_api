from django.shortcuts import render

from rest_framework import generics, permissions
from .serializers import SessionSerializer
from .models import Session
from .permissions import IsOwner

# PUT THIS ON FOR AUTHENTICATION!!
authentication_on = False

# Create your views here.
class CreateView(generics.ListCreateAPIView):
	"""This class defines the create behaviour of our rest api"""
	queryset = Session.objects.all()
	serializer_class = SessionSerializer
	
	if authentication_on:
		permission_classes = (permissions.IsAuthenticated, IsOwner)

	def perform_create(self, serializer):
		"""Save the post data when creating a new Session"""
		serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This handles the http GET, PUT and DELETE requests"""

	queryset = Session.objects.all()
	serializer_class = SessionSerializer
	if authentication_on:
		permission_classes= (permissions.IsAuthenticated, IsOwner)