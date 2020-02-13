import traceback

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.http import Http404, JsonResponse
from django.utils import timezone
from rest_framework import exceptions
from rest_framework.renderers import JSONRenderer

from account.models import Token
from utils.exceptions import AuthenticationFailed, BaseException, InvalidToken, UnknownException

procese_type = (list, tuple, dict, str, int, models.Model)


class MyAuthentication:
    def authenticate(self, request):
        header = self.authenticate_header(request)
        raw_token = self.get_raw_token(header)
        token = Token.objects.filter(token=raw_token).first()
        if not (token and token.verify()):
            raise InvalidToken
        if token.expired - timezone.now() < Token.token_expire:  # token快要过期了
            token.refresf_exp()
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


class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        ret = {'result': response, 'status': 200}
        if isinstance(response, procese_type):
            return JsonResponse(ret, encoder=DjangoJSONEncoder)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Todo auth role
        if request.path.startswith('/admin') or request.path == '/api/account/login/':
            return None
        if settings.DEBUG is True and not request.path.startswith('/api/workflow/'):
            return None
        try:
            user, token = MyAuthentication().authenticate(request)
            request._user = user
            request.token = token
        except Exception as e:
            return self.process_exception(request, e)
        return None

    def process_exception(self, request, exception):
        if settings.DEBUG is True:
            print(traceback.format_exc())
        if not isinstance(exception, BaseException):
            return JsonResponse(UnknownException().as_dict(), status=UnknownException().get_http_code())
        else:
            return JsonResponse(exception.as_dict(), status=exception.get_http_code())


class MyJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, procese_type):
            data = {'result': data, 'status': 200}
            renderer_context['response'].status_code = 200
            return super().render(data, accepted_media_type=accepted_media_type, renderer_context=renderer_context)
        else:
            return super().render(data, accepted_media_type=accepted_media_type, renderer_context=renderer_context)


def my_exception_handler(exc, context):
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()
    if isinstance(exc, exceptions.APIException):
        return JsonResponse({'status': exc.status_code, 'msg': exc.detail})
    else:
        return None
