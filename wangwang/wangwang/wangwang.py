import json
import traceback

from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.http import JsonResponse
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from rest_framework.authentication import BaseAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from account.models import Token
from utils.exceptions import AuthenticationFailed, BaseException, InvalidToken, UnknownException

procese_type = (list, tuple, dict, str, int, models.Model)


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        header = self.authenticate_header(request)
        raw_token = self.get_raw_token(header)
        token = Token.objects.filter(token=raw_token).first()
        if not (token and token.verify()):
            raise InvalidToken
        token.refresf_exp()
        request.user = token.user
        return token.user, token.token

    def get_raw_token(self, header):
        return header.split()[1]

    def authenticate_header(self, request):
        header = request.META.get('HTTP_AUTHORIZATION')
        if header is None:
            # Todo: another exception
            raise AuthenticationFailed
        parts = header.split()
        if len(parts) == 0 or len(parts) != 2:
            raise AuthenticationFailed
        return header


class MyMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        # Todo auth role

        # user = request.user
        if request.path.split('/')[1] == 'api':
            request._body = json.loads(request.body.decode())
        # if not user.is_anonymous and user.is_authenticated:
        #     return None
        # if request.path.split('/')[1] != 'api' or settings.AUTH_CONFIG.get('AUTH_EXCLUDE_PATH'):
        #     return None
        # try:
        #     MyAuthentication().authenticate(request)
        # except Exception as e:
        #     return self.process_exception(request, e)
        return None

    def process_exception(self, request, exception):
        if settings.DEBUG is True:
            print(traceback.format_exc())
        if not isinstance(exception, BaseException):
            return JsonResponse(UnknownException().as_dict(), status=UnknownException().get_http_code())
        else:
            return JsonResponse(exception.as_dict(), status=exception.get_http_code())

    def process_response(self, request, response):
        # if isinstance(response, models.Model):
        # response = str(response)
        ret = {'result': response, 'msg': 'success', 'status': 200}
        if isinstance(response, procese_type):
            return JsonResponse(ret, encoder=DjangoJSONEncoder)
        elif isinstance(response, Response) and response.status_code in [
                405,
        ]:
            data = {
                "msg": response.data['detail'],
                'status': response.status_code
            }  # msg also can be response.status_text
            return JsonResponse(data, status=response.status_code)
        return response


def update_last_login(sender, user, **kwargs):
    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])


class MyJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, procese_type) and renderer_context.get('response', {}).status_code == 200:
            data = {'result': data, 'msg': 'success', 'status': 200}
            return super().render(data, accepted_media_type=accepted_media_type, renderer_context=renderer_context)
        else:
            return super().render(data, accepted_media_type=accepted_media_type, renderer_context=renderer_context)
