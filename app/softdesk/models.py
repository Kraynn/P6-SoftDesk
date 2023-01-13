from django.db import models
from django.contrib.auth.models import User


"""
Choix du type de projets
"""
TYPES = [
    ("BACK", "back-end"), ("FRONT", "front-end"),
    ("IOS", "iOs"), ("ANDROID", "android"),
    ]

"""
Choix des tags, priorités et statut des problèmes
"""
TAGS = [("BUG", "bug"), ("UPDATE", "update"), ("TASK", "task")]
PRIORITIES = [("HIGH", "high"), ("MEDIUM", "medium"), ("LOW", "low")]
STATUS = [("ONGOING", "ongoing"), ("TO DO", "to do"), ("DONE", "done")]

"""
Choix des permissions et rôles des contributeurs
"""
PERMISSIONS = [ ("RESTRICTED", "contributor"),("ADMIN", "author"),]


"""
Objets Projets, Issues, Contributors et Commments
"""
class Projects(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=80, choices=TYPES)
    author_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)


class Contributors(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    project_id = models.ForeignKey(
        Projects, on_delete=models.CASCADE, blank=True, null=True)
    permission = models.CharField(
        max_length=80, choices=PERMISSIONS, default="RESTRICTED")
    role = models.CharField(max_length=255, blank=True, null=True)


class Issues(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, choices=TAGS)
    priority = models.CharField(max_length=255, choices=PRIORITIES)
    project_id = models.ForeignKey(
        Projects, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(
        max_length=255, choices=STATUS, blank=True, null=True)
    author_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='author_id',
        blank=True, null=True)
    assignee_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='assignee_id',
        blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    author_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    issue_id = models.ForeignKey(
        Issues, on_delete=models.CASCADE, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
