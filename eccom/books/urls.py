from django.urls import path,include
from rest_framework import routers
from .api.book_views import BookViewSet

router = routers.DefaultRouter()


router.register(r'book', BookViewSet)



urlpatterns = [
    path('', include(router.urls)),
]