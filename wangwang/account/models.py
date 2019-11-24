import binascii
import os

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .utils import user_avatar_path


class User(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()
    USERNAME_FIELD = 'username'

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('Designates whether this user should be treated as active. '
                    'Unselect this instead of deleting accounts.'),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    avatar = models.ImageField(_('avater'), upload_to=user_avatar_path, blank=True)
    organization = models.ForeignKey('Organization',
                                     verbose_name=_('organization'),
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     related_name='organization_users',
                                     blank=True)
    sex = models.CharField(_('sex'), max_length=10, choices=[('M', '男'), ('F', '女')], blank=True)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    class Meta:
        ordering = ['username']

    def __str__(self):
        name = '%s(%s)' % (self.username, self.get_full_name())
        return name.strip()


class Organization(models.Model):
    org_name = models.CharField(_('organization name'), max_length=50, unique=True)

    def __str__(self):
        return self.org_name


class Token(models.Model):
    token_length = settings.AUTH_CONFIG.get('TOKEN_LENGTH')
    token_expire = settings.AUTH_CONFIG.get('AUTH_TOKEN_EXPIRE')
    user = models.ForeignKey('User',
                             verbose_name=_("User"),
                             related_name='auth_token',
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True)
    created = models.DateTimeField(_('create time'), auto_now_add=True)
    expired = models.DateTimeField()
    token = models.TextField(_('token'))

    class Meta:
        ordering = ('user', )
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_key()
        return super().save(*args, **kwargs)

    def __str__(self):
        return 'Token for {} ({})'.format(self.user.username, self.token)

    def generate_key(self):
        return binascii.hexlify(os.urandom(self.token_length)).decode()

    def verify(self):
        return self.check_exp() and self.token_length == len(self.token.to_python())

    def check_exp(self):
        return timezone.now() < self.expired

    def refresh_token(self):
        self.token = self.generate_key()
        self.expired = timezone.now() + self.token_expire
        self.save(update_fields=['token', 'expired'])

    def refresf_exp(self):
        self.expired = timezone.now() + self.token_expire
        self.save(update_fields=['expired'])
