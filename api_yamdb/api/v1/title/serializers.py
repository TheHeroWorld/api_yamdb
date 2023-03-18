from rest_framework import serializers

from reviews.models import Category, Title, Genre
from api.v1.category_genres.serializers import (
    CategorySerializer,
    GenreSerializer
)
from reviews.validators import year_validator


class TitleWriteSerializer(serializers.ModelSerializer):
    year = serializers.IntegerField(validators=[year_validator])
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        fields = '__all__'
        model = Title


class TitleReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(
        read_only=True,
        many=True
    )
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title
