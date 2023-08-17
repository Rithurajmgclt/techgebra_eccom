from rest_framework import permissions

class AllowCreateUnauthenticated(permissions.BasePermission):
    """
    Custom permission to allow unauthenticated users to perform POST requests.
    """

    def has_permission(self, request, view):
        if request.method == 'POST' and not request.user.is_authenticated:
            return True
        elif request.user and request.user.is_authenticated:
            return True
        return False