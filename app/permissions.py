from rest_framework import permissions


class IsAuthorOrIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user and request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user and request.user.is_authenticated and request.user == obj.profile.user:
            return True


class ReadOnlyOrIsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user and request.user.is_authenticated and request.user.profile == obj.profile:
            return True