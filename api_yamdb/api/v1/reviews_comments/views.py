from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404

from api.v1.permissions import IsOwnerAdminModeratorOrReadOnly
from reviews.models import Review, Title
from .serializers import CommentSerializer, ReviewSerializer
from api.v1.mixins import NoPutModelViewSet


class ReviewViewSet(NoPutModelViewSet):
    """Вьюсет для класса Review."""

    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerAdminModeratorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(NoPutModelViewSet):
    """Вьюсет для класса Comment."""

    serializer_class = CommentSerializer
    permission_classes = (IsOwnerAdminModeratorOrReadOnly,)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)
