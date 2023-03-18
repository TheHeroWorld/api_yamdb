from django.urls import include, path
from rest_framework import routers

from .views import TitleViewSet


router_v_1 = routers.DefaultRouter()
router_v_1.register('titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('', include(router_v_1.urls)),
]
