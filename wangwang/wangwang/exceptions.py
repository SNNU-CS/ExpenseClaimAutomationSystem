from abc import ABCMeta

from .message import ErrorMsg


class BaseException(Exception):
    metaclass = ABCMeta

    def __init__(self, msg=None):
        super(BaseException, self).__init__()
        if msg is not None:
            self.msg = msg

    def get_http_code(self):
        return getattr(self, 'status_code', 200)

    def as_dict(self):
        ret = {'result': '', 'msg': getattr(self, 'msg', ''), 'status': getattr(self, 'status', '')}
        return ret


class UnknownException(BaseException):
    status_code = 200
    status = 1000
    msg = ErrorMsg.UNKNOWN_EXCEPTION


class AuthenticationFailed(BaseException):
    status_code = 401
    status = 1001
    msg = ErrorMsg.AUTH_FAILED


class InvalidToken(BaseException):
    status_code = 401
    status = 1002
    msg = ErrorMsg.INVALID_TOKEN
