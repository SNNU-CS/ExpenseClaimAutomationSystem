from django.utils.translation import gettext_lazy as _


class ErrorMsg:
    UNKNOWN_EXCEPTION = _('Unknown exception.')
    AUTH_FAILED = _('Auth failed.')
    INVALID_TOKEN = _('Token is invalid or expired.')
    OBJECT_DOES_NOT_EXIST = _("Objectd does not exists.")
    USERT_DOES_NOT_EXIST = _('Usert does not exists.')
    PASSWORD_INCORRECT = _('Password incorrect.')
    VALIDATION_ERROR = _('Valid input.')
