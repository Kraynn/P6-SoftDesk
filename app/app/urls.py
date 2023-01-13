from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from softdesk.views import (RegisterView,
    ProjectsViewSet,CommentsViewSet,ContributorsViewSet,IssuesViewSet)


router = routers.DefaultRouter()
router.register(r"", ProjectsViewSet, basename="projects")
router.register(r"^(?P<id>[^/.]+)/users",
 ContributorsViewSet, basename="users")
router.register(r"^(?P<id>[^/.]+)/issues",
 IssuesViewSet, basename="issues")
router.register(r"^(?P<id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/comments",
 CommentsViewSet, basename="comments")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('projects/', include(router.urls)),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]