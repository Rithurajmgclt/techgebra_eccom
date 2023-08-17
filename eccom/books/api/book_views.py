from rest_framework import viewsets

from custom.pagination import CustomPagination
from .book_serializers import BookSerializer
from .. models import Book
# from rest_framework.permissions import IsAuthenticated
from .permission import IsSuperuserOrReadOnly
from rest_framework.parsers import MultiPartParser

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing BOOK instances.
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsSuperuserOrReadOnly]## custom permission for super user
    parser_classes = [MultiPartParser]
    search_fields = ['title', 'author', 'description','ISBN']
    pagination_class = CustomPagination

    

