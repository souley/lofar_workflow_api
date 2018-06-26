from rest_framework import serializers
from .models import *#Session, PipelineConfiguration

# class SessionSerializer(serializers.ModelSerializer):
#     """ Serializer to map the Model instance into JSON format."""

#     #owner = serializers.ReadOnlyField(source = 'owner.username')

#     class Meta:
#         """Meta class to map serializer's fields with model fields"""
#         model = Session
#         fields = (\
#             'id', 'email', 'test_JSON_field', 'description', 'date_created', 'date_modified', 'status', 'pipeline_respone',\
#             "avg_freq_step", "avg_time_step", "do_demix", "demix_freq_step", \
#             "demix_time_step", "demix_sources", "select_NL", "parset", \
#             )
#         read_only_field = ('date_created', 'date_modified', 'status', 'pipeline_respone')

class SessionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    
    email = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(max_length=1000, default = "")
    pipeline = serializers.CharField(max_length=100, default="sksp")
    config = serializers.JSONField()

    status = serializers.CharField(max_length = 20, default = "unknown")
    pipeline_respone = serializers.CharField(max_length = 1000, default = "")
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Session.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.email)
        instance.description = validated_data.get('description', instance.description)
        instance.pipeline = validated_data.get('pipeline', instance.pipeline)
        instance.config = validated_data.get('config', instance.config)

        instance.status = validated_data.get('status', instance.status)
        instance.pipeline_response = validated_data.get('pipeline_response', instance.pipeline_response)
        
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.date_modified = validated_data.get('date_modified', instance.date_modified)

        instance.save()
        return instance