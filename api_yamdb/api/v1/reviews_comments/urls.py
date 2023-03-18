from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, ReviewViewSet


router_v_1 = routers.DefaultRouter()
router_v_1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)
router_v_1.register(
    r'titles/(?P<title_id>\d+)/reviews'
    r'/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('', include(router_v_1.urls)),
]
