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
        ret = {'msg': getattr(self, 'msg', ''), 'status': getattr(self, 'status', '')}
        return ret


class UnknownException(BaseException):
    status_code = 500
    status = 1000
    msg = ErrorMsg.UNKNOWN_EXCEPTION


class AuthenticationFailed(BaseException):
    status = 1001
    msg = ErrorMsg.AUTH_FAILED


class InvalidToken(BaseException):
    status = 1002
    msg = ErrorMsg.INVALID_TOKEN


class ObjectDoesNotExist(BaseException):
    status = 1003
    msg = ErrorMsg.OBJECT_DOES_NOT_EXIST


class UsertDoesNotExist(ObjectDoesNotExist):
    msg = ErrorMsg.USERT_DOES_NOT_EXIST


class PasswordIncorrect(ObjectDoesNotExist):
    status = 1004
    msg = ErrorMsg.PASSWORD_INCORRECT


class ValidationError(BaseException):
    status = 1005
    msg = ErrorMsg.VALIDATION_ERROR


class RoleDoesNoeExist(ObjectDoesNotExist):
    msg = ErrorMsg.ROLE_DOES_NOE_EXIST


class OrganizationDoesNotExist(ObjectDoesNotExist):
    msg = ErrorMsg.ORGANIZATION_DOES_NOT_EXIST


class UserIsNotActive(BaseException):
    status = 1006
    msg = ErrorMsg.USER_IS_NOT_ACTIVE


class OCRServiceUnavailable(BaseException):
    status = 1007
    msg = ErrorMsg.OCR_SERVICE_UNAVAILABLE


class InitStateNotConfig(BaseException):
    status = 1008
    msg = ErrorMsg.INIT_STATE_NOT_CONFIG


class WorkflowDoesNoeExist(ObjectDoesNotExist):
    msg = ErrorMsg.WORKFLOW_DOES_NOT_EXIST
