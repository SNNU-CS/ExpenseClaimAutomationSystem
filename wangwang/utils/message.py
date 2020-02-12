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
    USER_IS_NOT_ACTIVE = _('User is not active.')
    PASSWORD_MISMATCH = _('The two password fields didn\'t match.')
    OCR_SERVICE_UNAVAILABLE = _('OCR service unavailable.')
    INIT_STATE_NOT_CONFIG = _('该工作流尚未配置初始状态')
    WORKFLOW_DOES_NOT_EXIST = _('Workflow does not exists.')
