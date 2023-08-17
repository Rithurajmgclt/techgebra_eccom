from rest_framework import permissions

class IsSuperuserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow POST, PATCH, and DELETE only for authenticated superusers,
    while allowing read-only access for all authenticated users.
    """

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_superuser