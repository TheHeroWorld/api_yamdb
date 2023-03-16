from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, ReviewViewSet

v1_router = routers.DefaultRouters()
v1_router.register(
    'review',
    ReviewViewSet,
    basename='review'
)
v1_router.register(
    r'^review/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
