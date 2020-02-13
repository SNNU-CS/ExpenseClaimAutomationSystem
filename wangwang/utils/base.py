from django.db import models

from account.models import User


class BaseModel(models.Model):
    """
    基础model
    """
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        help_text='创建人',
    )
    created = models.DateTimeField('创建时间', auto_now_add=True)
    modified = models.DateTimeField('更新时间', auto_now=True)

    def get_dict(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        dict_result = {}
        import datetime
        for attr in fields:
            if isinstance(getattr(self, attr), datetime.datetime):
                dict_result[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr), datetime.date):
                dict_result[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            else:
                dict_result[attr] = getattr(self, attr)
        return dict_result

    class Meta:
        abstract = True
