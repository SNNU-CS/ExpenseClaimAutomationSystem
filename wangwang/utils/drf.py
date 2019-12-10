from rest_framework.response import Response

from .exceptions import ObjectDoesNotExist


def get_object(self):
    queryset = self.get_queryset().filter(pk=self.kwargs['pk'])
    if queryset.count() == 0:
        raise getattr(self, 'exc', ObjectDoesNotExist)
    return queryset.get()


def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    data = serializer.data
    self.perform_destroy(instance)
    return Response(data)
