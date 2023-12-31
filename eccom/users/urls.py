from django.urls import path,include
from rest_framework import routers
from .api.user_views import UserViewSet

router = routers.DefaultRouter()


router.register(r'user', UserViewSet)



urlpatterns = [
    path('', include(router.urls)),
]