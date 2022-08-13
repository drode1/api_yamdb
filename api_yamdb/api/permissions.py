from rest_framework import permissions


class IsCustomAdminUser(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.role == 'admin'


class IsUserOrAdmin(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user.username == obj.username
