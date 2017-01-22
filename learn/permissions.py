from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


class AdminOrReadOnly(permissions.BasePermission):
    """
    Read permission for everyone. Only admins can modify content.
    """
    def has_permission(self, request, view, obj=None):
        if request.method in permissions.SAFE_METHODS or request.user and request.user.is_staff:
            return True
        return False


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `user`.
        return obj.user == request.user
