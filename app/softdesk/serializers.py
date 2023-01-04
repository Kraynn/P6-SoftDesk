from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from softdesk.models import Projects, Comments, Issues 
 
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ["id", "description", "type", "author"]


class ProjectViewset(ModelViewSet):
 
    serializer_class = ProjectSerializer
 
    def get_queryset(self):
        return Projects.objects.all()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["id", "description", "author", "issue", "created_time"]


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = "__all__"