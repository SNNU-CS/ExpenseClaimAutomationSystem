class ConstantService:
    """一些常量"""
    def __init__(self):
        self.STATE_TYPE_NORMAL = 0  # 普通类型
        self.STATE_TYPE_START = 1  # 开始
        self.STATE_TYPE_END = 2  # 结束

        self.STATE_DISTRIBUTE_TYPE_ACTIVE = 0  # 主动接单
        self.STATE_DISTRIBUTE_TYPE_DIRECT = 1  # 直接处理(当前为多人的情况，都可以处理，而不需要先接单)
        self.STATE_DISTRIBUTE_TYPE_RANDOM = 2  # 随机分配
        self.STATE_DISTRIBUTE_TYPE_ALL = 3  # 全部处理

        self.PARTICIPANT_TYPE_BLANK = 0  # 无处理人
        self.PARTICIPANT_TYPE_PERSONAL = 1  # 个人
        self.PARTICIPANT_TYPE_MULTI = 2  # 多人
        self.PARTICIPANT_TYPE_DEPT = 3  # 部门
        self.PARTICIPANT_TYPE_ROLE = 4  # 角色
        self.PARTICIPANT_TYPE_ROBOT = 5  # 机器人，脚本
        self.PARTICIPANT_TYPE_MULTI_ALL = 6  # 多人全部处理(处理人为多个，且每个人都需要处理)，当状态处理人配置为全部处理，且处理人数大于1时，实际的处理人类型则为此

        self.TRANSITION_TYPE_COMMON = 0  # 常规流转
        self.TRANSITION_TYPE_TIMER = 1  # 定时器流转

        self.TRANSITION_ATTRIBUTE_TYPE_ACCEPT = 0  # 同意
        self.TRANSITION_ATTRIBUTE_TYPE_REFUSE = 1  # 拒绝
        self.TRANSITION_ATTRIBUTE_TYPE_OTHER = 2  # 其他

        self.FIELD_TYPE_STR = 0  # 字符串类型
        self.FIELD_TYPE_INT = 1  # 整形类型
        self.FIELD_TYPE_FLOAT = 2  # 浮点类型
        self.FIELD_TYPE_BOOL = 3  # 布尔类型
        self.FIELD_TYPE_DATE = 4  # 日期类型
        self.FIELD_TYPE_DATETIME = 5  # 日期时间类型
        self.FIELD_TYPE_RADIO = 6  # 单选框
        self.FIELD_TYPE_CHECKBOX = 7  # 多选框
        self.FIELD_TYPE_SELECT = 8  # 下拉列表
        self.FIELD_TYPE_MULTI_SELECT = 9  # 多选下拉列表
        self.FIELD_TYPE_TEXT = 10  # 文本域
        self.FIELD_TYPE_ATTACHMENT = 11  # 附件，多个附件使用逗号隔开。调用方自己实现上传功能

        # ???
        self.FIELD_TYPE_USERNAME = 60  # 用户名，前端展现时需要调用方系统获取用户列表
        self.FIELD_TYPE_MULTI_USERNAME = 70  # 多选用户名,多人情况逗号隔开，前端展现时需要调用方系统获取用户列表。loonflow只保存用户名

        self.FIELD_ATTRIBUTE_RO = 1  # 只读
        self.FIELD_ATTRIBUTE_REQUIRED = 2  # 必填
        self.FIELD_ATTRIBUTE_OPTIONAL = 3  # 可选

        self.TICKET_PERMISSION_HANDLE = 1  # 处理权限
        self.TICKET_PERMISSION_VIEW = 2  # 查看权限

        self.TICKET_BASE_FIELD_LIST = [
            'id', 'sn', 'title', 'state_id', 'parent_ticket_id', 'parent_ticket_state_id', 'participant_type_id',
            'participant', 'workflow_id', 'ticket_type_id', 'creator', 'is_deleted', 'gmt_created', 'gmt_modified'
        ]


CONSTANT_SERVICE = ConstantService()
