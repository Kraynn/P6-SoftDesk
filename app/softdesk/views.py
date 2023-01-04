from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from softdesk.models import Projects, Comments, Issues
from softdesk.serializers import ProjectSerializer, CommentSerializer, IssueSerializer
 

class ProjectViewset(ModelViewSet):
 
    serializer_class = ProjectSerializer
    def get_queryset(self):
        return Projects.objects.all()


class CommentsViewset(ModelViewSet):
 
    serializer_class = CommentSerializer
    def get_queryset(self):
        return Comments.objects.all()


class IssuesViewset(ModelViewSet):
 
    serializer_class = IssueSerializer
    def get_queryset(self):
        return Issues.objects.all()







# class ProjectAPIView(APIView):
 
#     def get(self, *args, **kwargs):
#         projects = Projects.objects.all()
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data)


# class CommentAPIView(APIView):
 
#     def get(self, *args, **kwargs):
#         comments = Comments.objects.all()
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)


# class IssueAPIView(APIView):
 
#     def get(self, *args, **kwargs):
#         issues = Issues.objects.all()
#         serializer = IssueSerializer(issues, many=True)
#         return Response(serializer.data)