from django.contrib.postgres.fields import JSONField
from django.db import models

from utils.base import BaseModel


class Workflow(BaseModel):
    """
    工作流
    """
    name = models.CharField('名称', max_length=50)
    description = models.CharField('描述', max_length=50)
    flowchart = models.FileField('流程图', upload_to='flowchart', blank=True, help_text='工作流的流程图,为了方便别人')
    # notices = models.CharField('通知', default='', blank=True, max_length=50, help_text='CustomNotice中的id.逗号隔开多个通知方式')
    # view_permission_check = models.BooleanField('查看权限校验', default=True, help_text='开启后，只允许工单的关联人(创建人、曾经的处理人)有权限查看工单')
    limit_expression = models.CharField(
        '限制表达式',
        max_length=1000,
        default='{}',
        blank=True,
        help_text='限制周期({"period":24} 24小时), 限制次数({"count":1}在限制周期内只允许提交1次), 限制级别({"level":1} 针对(1单个用户 2全局)限制周期限制次数,\
        默认特定用户);允许特定人员提交({"allow_persons":"zhangsan,lisi"}只允许张三提交工单,{"allow_depts":"1,2"}只允许部门id为1和2的用户提交工单，\
        {"allow_roles":"1,2"}只允许角色id为1和2的用户提交工单)'
    )
    display_form_str = models.CharField(
        '展现表单字段',
        max_length=10000,
        default='[]',
        blank=True,
        help_text='默认"[]"，用于用户只有对应工单查看权限时显示哪些字段,field_key的list的json,如["days","sn"],\
        内置特殊字段participant_info.participant_name:当前处理人信息(部门名称、角色名称)，state.state_name:当前状态的状态名,\
        workflow.workflow_name:工作流名称'
    )

    # default_notice_to = models.CharField('默认通知人', max_length=50, default='', \
    # blank=True, help_text='表单创建及结束时会发送相应通知信息')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '工作流'
        verbose_name_plural = '工作流'


class State(BaseModel):
    """
    状态记录, 变量支持通过脚本获取
    """
    STATE_TYPE = [(0, '普通类型'), (1, '初始状态'), (2, '结束状态')]
    PARTICIPANT_TYPE = [(0, '无处理人'), (1, '个人'), (2, '多人'), (3, '部门'), (4, '角色'), (5, '脚本'), (6, '参与人')]
    DISTRIBUTE_TYPE = [(0, '主动接单'), (1, '直接处理'), (2, '随机分配'), (4, '全部处理')]
    name = models.CharField('名称', max_length=50)
    workflow = models.ForeignKey(
        'Workflow', verbose_name='工作流', on_delete=models.SET_NULL, null=True, related_name='workflow_states'
    )
    sub_workflow = models.ForeignKey(
        'Workflow',
        verbose_name='子工作流',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='sub_workflow_states',
        help_text='如果需要在此状态启用子工单,请填写对应的工作流id'
    )
    order = models.IntegerField('状态顺序', default=0, help_text='用于工单步骤接口时，step上状态的顺序(因为存在网状情况，所以需要人为设定顺序),值越小越靠前')
    state_type = models.IntegerField(
        '状态类型id',
        default=0,
        choices=STATE_TYPE,
        help_text='0.普通类型 1.初始状态(用于新建工单时,获取对应的字段必填及transition信息) 2.结束状态(此状态下的工单不得再处理，即没有对应的transition)'
    )
    participant_type = models.IntegerField(
        '参与者类型id', default=1, blank=True, choices=PARTICIPANT_TYPE, help_text='0.无处理人,1.个人,2.多人,3.部门,4.角色,5.脚本,6.参与人'
    )  # Todo: add more type
    participant = models.CharField(
        '参与者',
        default='',
        blank=True,
        max_length=100,
        help_text='可以为空(无处理人的情况，如结束状态)、username、多个username(以,隔开)、部门id、角色id、变量(creator,creator_tl)、\
        脚本记录的id等，包含子工作流的需要设置处理人为loonrobot'
    )
    distribute_type = models.IntegerField(
        '分配方式',
        default=0,
        choices=DISTRIBUTE_TYPE,
        help_text='0.主动接单(如果当前处理人实际为多人的时候，需要先接单才能处理) 1.直接处理(即使当前处理人实际为多人，也可以直接处理)\
        2.随机分配(如果实际为多人，则系统会随机分配给其中一个人) 3.全部处理(要求所有参与人都要处理一遍,才能进入下一步)'
    )
    state_field_str = JSONField(
        '表单字段',
        default=dict,
        blank=True,
        help_text='json格式字典存储,包括读写属性1：只读，2：必填，3：可选. 示例：{"created_at":1,"title":2, "sn":1}, \
        内置特殊字段participant_info.participant_name:当前处理人信息(部门名称、角色名称)，state.state_name:当前状态的状态名,\
        workflow.workflow_name:工作流名称'
    )  # json格式存储,包括读写属性1：只读，2：必填，3：可选，4：不显示, 字典的字典

    def __str__(self):
        return '{}({})'.format(self.name, self.get_state_type_display())

    class Meta:
        verbose_name = '工作流状态'
        verbose_name_plural = '工作流状态'


class Transition(BaseModel):
    """
    工作流流转，定时器，条件(允许跳过)， 条件流转与定时器不可同时存在
    """
    TRANSITION_TYPE = [(0, '常规流转'), (1, '定时器流转')]
    ATTRIBUTE_TYPE = [(0, '同意'), (1, '拒绝'), (2, '其他')]
    name = models.CharField('操作', max_length=50)
    workflow = models.ForeignKey('Workflow', verbose_name='工作流id', on_delete=models.SET_NULL, null=True)
    transition_type = models.IntegerField(
        '流转类型', choices=TRANSITION_TYPE, default=0, help_text='0.常规流转，1.定时器流转,需要设置定时器时间'
    )
    timer = models.IntegerField('定时器(单位秒)', default=0, help_text='流转类型设置为定时器流转时生效,单位秒。处于源状态X秒后如果状态都没有过变化则自动流转到目标状态')
    source_state = models.ForeignKey(
        State, verbose_name='源状态', on_delete=models.CASCADE, related_name='source_transitions'
    )
    destination_state = models.ForeignKey(
        State, verbose_name='目的状态', on_delete=models.CASCADE, related_name='destination_transitions'
    )
    condition_expression = models.CharField(
        '条件表达式',
        max_length=1000,
        default='[]',
        help_text='流转条件表达式，根据表达式中的条件来确定流转的下个状态，格式为[{"expression":"{days} > 3 and {days}<10", "target_state_id":11}] \
        其中{}用于填充工单的字段key,运算时会换算成实际的值，当符合条件下个状态将变为target_state_id中的值,表达式只支持简单的运算或datetime/time运算.\
        loonflow会以首次匹配成功的条件为准，所以多个条件不要有冲突'
    )
    attribute_type = models.IntegerField('属性类型', choices=ATTRIBUTE_TYPE, default=0, help_text='属性类型，0.同意，1.拒绝，2.其他')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '工作流流转'
        verbose_name_plural = '工作流流转'


class CustomField(BaseModel):
    """自定义字段, 设定某个工作流有哪些自定义字段"""
    def default_boolean_field_display():
        return dict({"1": "是", "0": "否"})

    FIELD_TYPE = [(0, '字符串'), (1, '整形'), (2, '浮点型'), (3, '布尔'), (4, '时间'), (5, '日期时间'), (6, '单选框'), (7, '多选框'),
                  (8, '下拉列表'), (9, '多选下拉列表'), (10, '文本域'), (11, '附件')]
    workflow = models.ForeignKey('Workflow', on_delete=models.CASCADE, verbose_name='工作流')
    field_type = models.IntegerField(
        '类型',
        choices=FIELD_TYPE,
        help_text="""(0, '字符串'), (1, '整形'), (2, '浮点型'), (3, '布尔'), (4, '时间'), (5, '日期时间'), (6, '单选框'), (7, '多选框'),
                  (8, '下拉列表'), (9, '多选下拉列表'), (10, '文本域'),(11,'附件')"""
    )
    field_key = models.CharField('字段标识', max_length=50, help_text='字段类型请尽量特殊，避免与系统中关键字冲突')
    field_name = models.CharField('字段名称', max_length=50)
    order = models.IntegerField(
        '排序',
        default=0,
        help_text='工单基础字段在表单中排序为:流水号0,标题20,状态id40,状态名41,创建人80,创建时间100,更新时间120.前端展示工单信息的表单可以根据这个id顺序排列'
    )
    default_value = models.CharField(
        '默认值', null=True, blank=True, max_length=100, help_text='前端展示时，可以将此内容作为表单中的该字段的默认值'
    )
    description = models.CharField(
        '描述', max_length=100, blank=True, default='', help_text='字段的描述信息，对于非文本域字段可以将此内容作为placeholder'
    )
    field_template = models.TextField('文本域模板', default='', blank=True, help_text='文本域类型字段前端显示时可以将此内容作为字段的placeholder')
    boolean_field_display = JSONField(
        '布尔类型显示名',
        default=default_boolean_field_display,
        blank=True,
        help_text='当为布尔类型时候，可以支持自定义显示形式。{"1":"是","0":"否"}或{"1":"需要","0":"不需要"}，注意数字也需要引号'
    )
    field_choice = JSONField(
        'radio、checkbox、select的选项',
        default=dict,
        blank=True,
        help_text='radio,checkbox,select,multiselect类型可供选择的选项，格式为json如:{"1":"中国", "2":"美国"},注意数字也需要引号'
    )

    class Meta:
        verbose_name = '工作流自定义字段'
        verbose_name_plural = '工作流自定义字段'


# def upload_workflow_script(instance, filename):
#     """
#     因为脚本中可能会存在一些私密信息，如账号密码等，所以重命名文件，避免可以直接下载此文件
#     :param instance:
#     :param filename:
#     :return:
#     """
#     upload_to = 'workflow_script'
#     ext = filename.split('.')[-1]
#     if ext != 'py':
#         raise Exception('只支持python脚本')
#     filename = '{}.{}'.format(uuid.uuid1(), ext)
#     return os.path.join(upload_to, filename)

# class WorkflowScript(BaseModel):
#     """
#     流程中执行的脚本
#     """
#     name = models.CharField('名称', max_length=50)
#     saved_name = models.FileField(
#         '存储的文件名',
#         upload_to=upload_workflow_script,
#         help_text='请上传python脚本,media/workflow_script/demo_script.py为示例脚本，请参考编写'
#     )
#     description = models.CharField('描述', max_length=100, null=True, blank=True)
#     is_active = models.BooleanField('可用', default=True, help_text='此处可用时，才允许实际执行')

#     class Meta:
#         verbose_name = '工作流脚本'
#         verbose_name_plural = '工作流脚本'
