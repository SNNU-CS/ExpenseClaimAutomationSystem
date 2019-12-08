from django.apps import AppConfig

from .signals import user_logged_in


class AccountConfig(AppConfig):
    name = 'account'

    def ready(self):
        from .models import update_last_login
        user_logged_in.connect(update_last_login, dispatch_uid='update_last_login')
