from rest_framework import viewsets

from custom.pagination import CustomPagination
from .cart_serializer import CartSerializer,CartListSerializer
from .. models import Cart
from rest_framework.permissions import IsAuthenticated

class CartViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing cart instances.
    """
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return CartListSerializer
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return CartSerializer
        return CartSerializer 
