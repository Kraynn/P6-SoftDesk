from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from softdesk.permission import (
    ProjectPermission, IssuesPermission, CommentsPermission)
from softdesk.serializers import (
    ProjectsSerializer,CommentsSerializer,
    ContributorsSerializer,IssuesSerializer,RegisterSerializer)
from softdesk.models import Projects, Comments, Contributors, Issues


"""
View de création d'utilisateur
"""
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
Viewset des différents objects de l'application
"""
class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [permissions.IsAuthenticated, ProjectPermission]

    def get_queryset(self):
        return Projects.objects.filter(author_user_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)


class IssuesViewSet(viewsets.ModelViewSet):
    serializer_class = IssuesSerializer
    permission_classes = [permissions.IsAuthenticated, IssuesPermission]

    def get_queryset(self):
        id_project = get_object_or_404(Projects, pk=self.kwargs['id'])
        return Issues.objects.filter(project_id=id_project)

    def perform_create(self, serializer):
        id_project = get_object_or_404(Projects, pk=self.kwargs['id'])
        serializer.save(project_id=id_project)
        serializer.save(author_user_id=self.request.user)


class ContributorsViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id_project = get_object_or_404(Projects, pk=self.kwargs['id'])
        return Contributors.objects.filter(projet_id=id_project)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated, CommentsPermission]

    def get_queryset(self):
        issue = self.kwargs.get('issue_id')
        id_project = get_object_or_404(Projects, pk=self.kwargs['id'])
        id_issues = Issues.objects.filter(project_id=id_project)
        id_issue = id_issues.get(pk=issue)
        return Comments.objects.filter(issue_id=id_issue)

    def perform_create(self, serializer):
        issue = self.kwargs.get('issue_id')
        id_project = get_object_or_404(Projects, pk=self.kwargs['id'])
        id_issues = Issues.objects.filter(project_id=id_project)
        id_issue = id_issues.get(pk=issue)
        serializer.save(issue_id=id_issue)
        serializer.save(author_user_id=self.request.user)








