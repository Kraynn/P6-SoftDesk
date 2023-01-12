from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comments, Contributors, Projects, Issues


"""
Serializer de création d'utilisateur
"""
class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}


"""
Serializer pour les différents objets de l'application
"""
class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = "__all__"


class ContributorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributors
        fields = "__all__"


class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = "__all__"


class IssuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issues
        fields = "__all__"




