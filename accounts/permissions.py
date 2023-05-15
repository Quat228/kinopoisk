from rest_framework import permissions


class ReadOnlyOrIsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user and request.user.is_authenticated and request.user == obj.user:
            return True

