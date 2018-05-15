from rest_framework import serializers
from .models import Session

class SessionSerializer(serializers.ModelSerializer):
	""" Serializer to map the Model instance into JSON format."""

	owner = serializers.ReadOnlyField(source = 'owner.username')

	class Meta:
		"""Meta class to map serializer's fields with model fields"""
		model = Session
		fields = ('id', 'name', 'owner', 'pipeline_id', 'obs_id', 'date_created', 'date_modified')
		read_only_field = ('date_created', 'date_modified')