from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from api.v1.permissions import IsAdminOrReadOnly


class PatchModelMixin:
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        queryset = self.filter_queryset(self.get_queryset())
        if queryset._prefetch_related_lookups:
            instance._prefetched_objects_cache = {}
            instance._prefetch_related_objects(
                [instance],
                *queryset._prefetch_related_lookups
            )
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


class NoPutModelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    PatchModelMixin,
    viewsets.GenericViewSet
):
    pass


class CategoryGenreViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (SearchFilter, )
    search_fields = ('name',)
    lookup_field = 'slug'
