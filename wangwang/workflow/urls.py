from django.urls import include, path
from rest_framework import routers

from .views import CustomFieldView, StateView, TransitionView, WorkflowView

router = routers.SimpleRouter()
router.register(r'workflows', WorkflowView)
router.register(r'states', StateView)
router.register(r'transitions', TransitionView)
router.register(r'fields', CustomFieldView)

urlpatterns = [
    path('', include(router.urls), name='workflows'),
]
