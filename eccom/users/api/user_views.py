from rest_framework import viewsets
from django.contrib.auth.models import User

from custom.pagination import CustomPagination
from .user_serializers import UserSerializer
# from rest_framework.permissions import IsAuthenticated
from .permissions import AllowCreateUnauthenticated

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = CustomPagination
    permission_classes = [AllowCreateUnauthenticated]
