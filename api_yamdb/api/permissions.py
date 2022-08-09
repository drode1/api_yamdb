from rest_framework import permissions

# Получаю admin из кастомной модели User
admin = ''


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (admin == request.user
                or request.method in permissions.SAFE_METHODS)
