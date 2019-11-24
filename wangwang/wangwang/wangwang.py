from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from .exceptions import BaseException, UnknownException
from account.models import User, Token
from django.conf import settings
from .exceptions import AuthenticationFailed, InvalidToken


class MyAuthentication:
    def authenticate(self, request):
        header = request.META.get('HTTP_AUTHORIZATION')
        if header is None:
            # Todo: another exception
            raise AuthenticationFailed
        raw_token = self.get_raw_token(header)
        token = Token.objects.get(token=raw_token)
        if not token.verify():
            raise InvalidToken
        token.refresf_exp()
        request.user = token.user

    def get_raw_token(self, header):
        parts = header.split()
        if len(parts) == 0 or len(parts) != 2:
            raise AuthenticationFailed
        return parts[1]


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = request.user
        if not user.is_anonymous and user.is_authenticated:
            return None
        if request.path in settings.AUTH_CONFIG.get('AUTH_EXCLUDE_PATH'):
            return None
        MyAuthentication().authenticate(request)

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
