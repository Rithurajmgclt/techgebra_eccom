from rest_framework import serializers
from ..models import Cart
from books .api.book_serializers import BookSerializer


class CartListSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True)
    class Meta:
        model=Cart
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields = '__all__'

