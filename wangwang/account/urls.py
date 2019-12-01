from django.urls import path

from .views import AuthView

urlpatterns = [
    path('login/', AuthView.as_view(), name='user-login'),
    # path('', include(router.urls)),
]
