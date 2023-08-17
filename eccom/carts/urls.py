from django.urls import path,include
from rest_framework import routers
from .api .cart_views import CartViewSet

router = routers.DefaultRouter()


router.register(r'cart', CartViewSet)



urlpatterns = [
    path('', include(router.urls)),
]