from django.urls import path, include
from rest_framework import routers
from .views import GenreViewSet, CategoryViewSet, TitlesViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('genres', GenreViewSet, basename='genres')
router.register('categories', CategoryViewSet, basename='categories')
router.register('titles', TitlesViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router.urls)),
]
