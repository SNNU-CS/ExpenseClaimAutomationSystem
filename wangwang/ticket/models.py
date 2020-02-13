from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone

from utils.base import BaseModel
from workflow.models import State, Transition, Workflow
from account.models import User


def default_sn():
    now = timezone.localtime(timezone.now())
    return now.strftime("%Y%m%d%H%M%S")


class TicketRecord(BaseModel):
    """
    工单记录
    """
    title = models.CharField('标题', max_length=500, blank=True, default='', help_text="工单的标题")
    workflow = models.ForeignKey(Workflow, null=True, on_delete=models.SET_NULL, help_text='关联的流程')
    sn = models.CharField('流水号', default=default_sn, max_length=25, help_text="工单的流水号")
    state = models.ForeignKey(
        State,
        null=True,
        on_delete=models.SET_NULL,
        related_name='state_tickets',
        verbose_name='当前状态',
        help_text='与workflow.State关联'
    )
    parent_ticket = models.ForeignKey(
        'self',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name='父工单',
        related_name='state_parent_tickets',
        help_text='TicketRecord关联'
    )
    parent_ticket_state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        verbose_name='对应父工单状态',
        null=True,
        blank=True,
        help_text='与workflow.State关联,子工单是关联到父工单的某个状态下的'
    )
    participant_type = models.IntegerField(
        '当前处理人类型', choices=State.PARTICIPANT_TYPE, default=0, help_text='0.无处理人,1.个人,2.多人,3.部门,4.角色'
    )
    participant = models.CharField(
        '当前处理人',
        max_length=100,
        default='',
        blank=True,
        help_text='可以为空(无处理人的情况，如结束状态)、username、多个username(以,隔开)、部门id、角色id、脚本文件名等'
    )
    ticket_data = JSONField('工单数据', default=dict, blank=True, help_text='可以用于记录当前表单数据，json格式')
    is_end = models.BooleanField('已结束', default=False, help_text='工单是否已处于结束状态')

    def __str__(self):
        return self.sn

    class Meta:
        verbose_name = '工单记录'
        verbose_name_plural = '工单记录'


class TicketFlowLog(models.Model):
    """
    工单流转日志
    """
    created = models.DateTimeField('创建时间', auto_now_add=True)
    ticket = models.ForeignKey(TicketRecord, on_delete=models.SET_NULL, null=True)
    transition = models.ForeignKey(Transition, on_delete=models.SET_NULL, verbose_name='流转', null=True)
    suggestion = models.CharField('处理意见', max_length=1000, default='', blank=True)
    participant_type = models.IntegerField(
        '处理人类型', choices=State.PARTICIPANT_TYPE, help_text='constant_service中定义', default=0
    )
    participant = models.CharField('处理人', max_length=50, default='', blank=True)
    state = models.ForeignKey(State, verbose_name='当前状态', null=True, blank=True, on_delete=models.SET_NULL)
    ticket_data = JSONField('工单数据', default=dict, blank=True, help_text='可以用于记录当前表单数据，json格式')

    def save(self, *args, **kwargs):
        if not self.state:
            self.state = self.transition.destination_state
        super(TicketFlowLog, self).save(*args, **kwargs)  # Call the real save() method

    class Meta:
        verbose_name = '工单流转日志'
        verbose_name_plural = '工单流转日志'


def file_upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/files/<id>/<20200213>/<file_name>
    now = timezone.localtime(timezone.now())
    date = now.strftime("%Y%m%d")
    print(instance)
    return 'files/{0}/{1}/{2}'.format(instance.creator.id, date, filename)


class TicketFile(models.Model):
    file = models.FileField(upload_to=file_upload_path, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, help_text='创建人')
    created = models.DateTimeField('创建时间', auto_now_add=True)


# class TicketCustomField(BaseModel):
#     """
#     工单自定义字段， 工单自定义字段实际的值。
#     """
#     name = models.CharField(u'字段名', max_length=50)
#     field_key = models.CharField(u'字段标识', max_length=50)
#     ticket_id = models.IntegerField(u'工单id')
#     field_type_id = models.IntegerField(u'字段类型', help_text='见service.constant_service中定义')
#     char_value = models.CharField('字符串值', max_length=1000, default='', blank=True)
#     int_value = models.IntegerField('整形值', default=0, blank=True)
#     float_value = models.FloatField('浮点值', default=0.0, blank=True)
#     bool_value = models.BooleanField('布尔值', default=False, blank=True)
#     # date_value = models.DateField('日期值', default='0001-01-01', blank=True)
#     date_value = models.DateField('日期值', default=datetime.datetime.strptime('0001-01-01', "%Y-%m-%d"), blank=True)
#     # datetime_value = models.DateTimeField('日期时间值', default='0001-01-01 00:00:00', blank=True)
#     datetime_value = models.DateTimeField(
#         '日期时间值', default=datetime.datetime.strptime('0001-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'), blank=True
#     )
#     # time_value = models.TimeField('时间值', default='00:00:01', blank=True)
#     time_value = models.TimeField('时间值', default=datetime.datetime.strptime('00:00:01', '%H:%M:%S'), blank=True)
#     radio_value = models.CharField('radio值', default='', max_length=50, blank=True)
#     checkbox_value = models.CharField('checkbox值', default='', max_length=50, blank=True, help_text='逗号隔开多个选项')
#     select_value = models.CharField('下拉列表值', default='', max_length=50, blank=True)
#     multi_select_value = models.CharField('多选下拉列表值', default='', max_length=50, blank=True, help_text='逗号隔开多个选项')
#     text_value = models.TextField('文本值', default='', blank=True)
#     username_value = models.CharField('用户名', max_length=50, default='', blank=True)
#     multi_username_value = models.CharField('多选用户名', max_length=1000, default='', blank=True)

#     class Meta:
#         verbose_name = '工单自定义字段'
#         verbose_name_plural = '工单自定义字段'
