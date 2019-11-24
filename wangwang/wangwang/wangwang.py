from django.utils import timezone
from rest_framework.authentication import BaseAuthentication
from django.utils.deprecation import MiddlewareMixin
from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from .exceptions import BaseException, UnknownException


class MyMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if not isinstance(exception, BaseException):
            return JsonResponse(UnknownException().as_dict(), status=UnknownException().get_http_code())
        else:
            return JsonResponse(exception.as_dict(), status=exception.get_http_code())

    def process_response(self, request, response):
        procese_type = (list, tuple, dict, str, int, models.Model)
        # if isinstance(response, models.Model):
        # response = str(response)
        ret = {'result': response, 'msg': 'success', 'status': 200}
        if isinstance(response, procese_type):
            return JsonResponse(ret, encoder=DjangoJSONEncoder)
        return response


def update_last_login(sender, user, **kwargs):
    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])
