from django.urls import include, path
from rest_framework import routers

from .views import TicketView

router = routers.SimpleRouter()
router.register(r'tickets', TicketView)

urlpatterns = [
    path('', include(router.urls), name='tickets'),
]
