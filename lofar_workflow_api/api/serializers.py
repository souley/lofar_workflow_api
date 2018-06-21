from rest_framework import serializers
from .models import *#Session, PipelineConfiguration

class SessionSerializer(serializers.ModelSerializer):
	""" Serializer to map the Model instance into JSON format."""

	#owner = serializers.ReadOnlyField(source = 'owner.username')

	class Meta:
		"""Meta class to map serializer's fields with model fields"""
		model = Session
		fields = ('id', 'name', 'date_created', 'date_modified') #'owner', 'pipeline_conf', 'observation', 
		read_only_field = ('date_created', 'date_modified')

# class PipelineConfigurationSerializer(serializers.ModelSerializer):

# 	#owner = serializers.ReadOnlyField(source = 'owner.username')

# 	class Meta:
# 		model = PipelineConfiguration
# 		fields = ('id', 'name', 'some_setting_1', 'some_setting_2') #'owner', 
# 		read_only_field = ('date_created', 'date_modified')


# class ObservationSerializer(serializers.ModelSerializer):

# 	#owner = serializers.ReadOnlyField(source = 'owner.username')

# 	class Meta:
# 		model = Observation
# 		fields = ('id', 'name', 'some_identifier') # 'owner', 
# 		read_only_field = ('date_created', 'date_modified')