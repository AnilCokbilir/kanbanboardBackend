from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Tasks
from .serializers import TasksSerializer
# Create your views here.
class TasksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tasks.objects.all().order_by('due_date')
    serializer_class = TasksSerializer
    permission_classes = [] #permissions.IsAuthenticated
