from django.urls import include, path
from rest_framework import routers

from .views import AuthView, OrganizationViewSet, RoleViewSet, UserSelfView, UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'organizations', OrganizationViewSet)
urlpatterns = [
    path('login/', AuthView.as_view(), name='user-login'),
    path('self/', UserSelfView.as_view(), name='user-self'),
    path('', include(router.urls), name='user'),
]
