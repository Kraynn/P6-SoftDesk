from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from softdesk.models import Projects, Comments, Issues 


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        )
        extra_kwargs = {'password': {'write_only': True}}

        def validate_name(self, value):
            if User.objects.filter(username=value).exists():
                raise serializers.ValidationError('Ce nom existe déjà!')
            return value

        def create(self, data):
            user = User.objects.create(
                username=data["username"],
                email=data["email"],
                first_name=data["first_name"],
                last_name=data["last_name"],
            )
            user.set_password(data["password"])
            user.save()

            return user
 
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
