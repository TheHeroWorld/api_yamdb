from django.db.models import Avg

from reviews.models import Title
from api.v1.permissions import IsAdminOrReadOnly
from api.v1.title.filters import TitleFilter
from .serializers import (
    TitleReadSerializer,
    TitleWriteSerializer,
)
from api.v1.mixins import NoPutModelViewSet


class TitleViewSet(NoPutModelViewSet):
    """Вьюсет для класса Title."""

    queryset = Title.objects.annotate(rating=Avg('reviews__score')).all()
    filterset_class = TitleFilter
    permission_classes = (IsAdminOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return TitleWriteSerializer
        return TitleReadSerializer
