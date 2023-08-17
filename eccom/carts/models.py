from django.db import models
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)