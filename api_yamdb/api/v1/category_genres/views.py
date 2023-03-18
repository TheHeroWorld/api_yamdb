from .serializers import CategorySerializer, GenreSerializer

from reviews.models import Category, Genre
from api.v1.mixins import CategoryGenreViewSet


class CategoryViewSet(CategoryGenreViewSet):
    """Вьюсет для класса Category."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(CategoryGenreViewSet):
    """Вьюсет для класса Genre."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
