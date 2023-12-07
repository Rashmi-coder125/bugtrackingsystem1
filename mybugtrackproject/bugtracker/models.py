from django.db import models
from django.contrib.auth.models import User  # Import the User model

class Bug(models.Model):
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_bugs')
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100, default='Open')  # e.g., Open, In Progress, Closed
    project = models.CharField(max_length=100)  # Project name or ID
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    priority = models.CharField(max_length=50, default='Medium')  # e.g., Low, Medium, High

    def __str__(self):
        return f"{self.title} - {self.status}"
