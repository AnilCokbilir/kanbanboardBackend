from turtle import title
from unicodedata import category
from django.db import models
import uuid
import datetime
# Create your models here.
urgency_choices = (
    ("LOW", "Low"),
    ("MEDIUM", "Medium"),
    ("HIGH", "High"),  
)

category_choices = (
    ("IT", "It"),
    ("SALES", "Sales"),
    ("FINANCE", "Finance"),
    ("MANAGEMENT", "Management")
)


class Tasks(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=30)
    assigned_to = models.CharField(max_length=30)
    due_date = models.DateField(null=True, blank=True)
    urgency = models.CharField(max_length=30, choices=urgency_choices, default="MEDIUM")
    #id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True)
    category = models.CharField(max_length=30, choices=urgency_choices, default="IT")