from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return (request.method in permissions.SAFE_METHODS
                    or request.user.role == 'admin')
        else:
            return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated
                or request.user.is_superuser
                or request.user.role == 'admin'
                or request.method in permissions.SAFE_METHODS)


class IsCustomAdminUser(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.role == 'admin'
