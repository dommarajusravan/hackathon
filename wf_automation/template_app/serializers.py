from rest_framework import serializers
from .models import templates, deployment

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = templates
#        fields = '__all__'

class DeploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = deployment
#        fields = '__all__'
