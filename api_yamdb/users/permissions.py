from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminAndSuperuserOnly(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and (
                request.user.is_admin
                or request.user.is_superuser
            )
        )


class AuthenticatedPrivilegedUsersOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or obj.author == request.user
            or request.user.is_admin
            or request.user.is_superuser
            or request.user.is_moderator
        )


class ListOrAdminModeratOnly(BasePermission):
    """Разрешает получения списка всем и редактирование
    только  администратору/суперпользователю"""

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
            or request.user.is_authenticated
            and request.user.is_admin
        )
