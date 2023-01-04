from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

TYPES = [
    ("BACK", "back-end"),
    ("FRONT", "front-end"),
    ("IOS", "iOs"),
    ("ANDROID", "android"),
    ]

TAG = [("BUG", "bug"), ("UPDATE", "update"), ("TASK", "task")]

PRIORITY = [("HIGH", "high"), ("MEDIUM", "medium"), ("LOW", "low")]

STATUS = [("ONGOING", "ongoing"), ("TO DO", "to do"), ("DONE", "done")]


class Projects(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=7, choices=TYPES)              
    author = models.ForeignKey(AUTH_USER_MODEL,
        on_delete=models.CASCADE, null=True)


class Issues(models.Model):
    title = models.CharField(max_length=80)
    desc = models.CharField(max_length=255, null=True)
    tag = models.CharField(max_length=16, null=True, blank=True, choices=TAG)
    priority = models.CharField(max_length=16, null=True, blank=True)
    project = models.ForeignKey(
        to=Projects,on_delete=models.CASCADE, related_name="issues")
    status = models.CharField(
        max_length=16, null=True, blank=True, choices=STATUS)
    author = models.ForeignKey(AUTH_USER_MODEL,
        on_delete=models.CASCADE,null=True, related_name="written_issues")
    assignee = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
        related_name="assignee_to_issues")
    created_time = models.DateTimeField(auto_now_add=True, null=True)


class Comments(models.Model):
    description = models.CharField(max_length=255)
    author = models.ForeignKey(AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name='comments')
    issue = models.ForeignKey(
        to=Issues,
        on_delete=models.CASCADE, related_name='comments')
    created_time = models.DateTimeField(auto_now_add=True, null=True)


class Contributors(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='contributing_users', null=True)
    project = models.ForeignKey(
        to=Projects, on_delete=models.CASCADE, related_name='projects',
        null=True)
    role = models.CharField(max_length=80, null=True, blank=True)
