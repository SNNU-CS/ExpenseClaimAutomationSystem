from django.utils.translation import gettext_lazy as _


class ErrorMsg:
    UNKNOWN_EXCEPTION = _('Unknown exception.')
    AUTH_FAILED = _('Auth failed.')
    INVALID_TOKEN = _('Token is invalid or expired.')
    OBJECT_DOES_NOT_EXIST = _("Object does not exists.")
    USERT_DOES_NOT_EXIST = _('User does not exists.')
    PASSWORD_INCORRECT = _('Password incorrect.')
    VALIDATION_ERROR = _('Valid input.')
    ROLE_DOES_NOE_EXIST = _('Role does not exists.')
    ORGANIZATION_DOES_NOT_EXIST = _('Organization does not exists.')
