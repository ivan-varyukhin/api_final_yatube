from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet
from .views import GroupViewSet, PostViewSet

router_v1 = DefaultRouter()

router_v1.register(r'v1/posts', PostViewSet, basename='posts')
router_v1.register(r'v1/follow', FollowViewSet, basename='follow')
router_v1.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register(r'v1/groups', GroupViewSet, basename='group')

urlpatterns = [
    path(r'', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
