from django.urls import include, path
from rest_framework import routers

from .views import AuthView, UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
    path('login/', AuthView.as_view(), name='user-login'),
    path('', include(router.urls), name='user'),
]
