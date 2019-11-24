from django.utils.translation import gettext_lazy as _


class ErrorMsg:
    UNKNOWN_EXCEPTION = _('Unknown exception.')
    AUTH_FAILED = _('Auth failed.')
    INVALID_TOKEN = _('Token is invalid or expired.')
