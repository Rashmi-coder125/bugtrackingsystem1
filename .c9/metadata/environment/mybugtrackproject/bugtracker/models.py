{"filter":false,"title":"models.py","tooltip":"/mybugtrackproject/bugtracker/models.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":20,"column":4},"end":{"row":20,"column":87},"action":"remove","lines":["reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)"],"id":8}],[{"start":{"row":0,"column":0},"end":{"row":27,"column":0},"action":"remove","lines":["from django.conf import settings","from django.db import models","","class Project(models.Model):","    title = models.CharField(max_length=100)","","    def __str__(self):","        return self.title","","class Status(models.Model):","    name = models.CharField(max_length=50)","","    def __str__(self):","        return self.name","","class Bug(models.Model):","    title = models.CharField(max_length=100)","    description = models.TextField()","    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)","    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)","    ","    created_at = models.DateTimeField(auto_now_add=True)","    updated_at = models.DateTimeField(auto_now=True)","    ","","    def __str__(self):","        return self.title",""],"id":9},{"start":{"row":0,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["from django.db import models","from django.contrib.auth.models import User  # Import the User model","","class Bug(models.Model):","    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_bugs')","    title = models.CharField(max_length=100)","    description = models.TextField()","    status = models.CharField(max_length=100, default='Open')  # e.g., Open, In Progress, Closed","    project = models.CharField(max_length=100)  # Project name or ID","    created_at = models.DateField(auto_now_add=True)","    updated_at = models.DateField(auto_now=True)","    priority = models.CharField(max_length=50, default='Medium')  # e.g., Low, Medium, High","","    def __str__(self):","        return f\"{self.title} - {self.status}\"",""]}]]},"ace":{"folds":[],"scrolltop":44.5,"scrollleft":0,"selection":{"start":{"row":7,"column":44},"end":{"row":7,"column":44},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":2,"state":"start","mode":"ace/mode/python"}},"timestamp":1702056304036,"hash":"a93bfa9b08a034e43fd0bf6296784df9ad3a497d"}