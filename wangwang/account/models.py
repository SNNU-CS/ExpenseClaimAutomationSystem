from django.contrib.auth.models import AbstractUser
from django.db import models

from .utils import user_avatar_path


class User(AbstractUser):
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True)
    organization = models.ForeignKey('Organization', on_delete=models.SET_NULL, null=True)
    sex = models.CharField(max_length=1, choices=[('M', '男'), ('F', '女')], blank=True)

    class Meta:
        ordering = ['username']

    def __str__(self):
        name = '%s(%s)' % (self.username, self.get_full_name())
        return name.strip()


class Organization(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
