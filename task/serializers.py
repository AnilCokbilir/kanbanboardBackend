from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Tasks

class TasksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id','name', 'title', 'description', 'assigned_to', 'due_date', 'urgency', 'category']
