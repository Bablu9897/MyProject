from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import App, Task
from .serializers import AppSerializer, TaskSerializer, UserSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]
