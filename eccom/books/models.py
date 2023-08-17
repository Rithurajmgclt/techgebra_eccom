
from django.db import models



# Create your models here
class Book(models.Model):
    title                = models.CharField(max_length=200)
    author               = models.CharField(max_length=100)
    publication_date     = models.DateField()
    ISBN                 = models.CharField(max_length=100)
    description          = models.TextField()
    image                = models.ImageField(upload_to='images/product',null=True,blank=True)  



