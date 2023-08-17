from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = ['id','title','author','publication_date','ISBN','description','image']