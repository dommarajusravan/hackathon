# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import templates, deployment
from .serializers import TemplateSerializer, DeploymentSerializer


# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You're at the template index.")

class DeploymentViewSet(viewsets.ModelViewSet):
    queryset = deployment.objects.all()
    serializer_class = DeploymentSerializer

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = templates.objects.all()
    serializer_class = TemplateSerializer
