from rest_framework import serializers

from utils.exceptions import WorkflowDoesNoeExist
from utils.service import CONSTANT_SERVICE
from workflow.models import State, Workflow
from workflow.serializers import StateSerializer, TransitionSerializer, WorkflowSerializer

from .models import TicketFile, TicketFlowLog, TicketRecord


class TicketRecordSerializer(serializers.ModelSerializer):
    workflow = WorkflowSerializer()
    state = StateSerializer()
    creator = serializers.SerializerMethodField()
    participant_type = serializers.CharField(source='get_participant_type_display')

    def get_creator(self, obj):
        return obj.creator.username

    class Meta:
        model = TicketRecord
        fields = '__all__'


class CreateTicketRecordSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, write_only=True, help_text='流程的标题')
    workflow = serializers.IntegerField(required=True, write_only=True)
    participant_type = serializers.ChoiceField(
        State.PARTICIPANT_TYPE,
        required=False,
        help_text="默认为个人,(0, '无处理人'), (1, '个人'), (2, '多人'), (3, '部门'), (4, '角色'), (5, '脚本'), (6, '参与人')"
    )
    participant = serializers.CharField(
        required=False, help_text='默认为创建人,可以为空(无处理人的情况，如结束状态)、username、多个username(以,隔开)、角色、脚本文件名等'
    )
    ticket_data = serializers.JSONField(required=True, help_text='表单数据')

    def validate_workflow(self, value):
        workflow = Workflow.objects.filter(pk=value).first()
        if not workflow:
            raise WorkflowDoesNoeExist
        return workflow

    def validate(self, validated_data):
        validated_data['participant_type'] = validated_data.get(
            'participant_type', CONSTANT_SERVICE.PARTICIPANT_TYPE_PERSONAL
        )
        validated_data['state'] = validated_data['workflow'].get_init_state()
        return validated_data

    def to_representation(self, obj):
        return TicketRecordSerializer(obj).data

    class Meta:
        model = TicketRecord
        exclude = ('sn', 'is_end', 'state')


class TicketFlowLogSerializer(serializers.ModelSerializer):
    transition = TransitionSerializer()

    class Meta:
        model = TicketFlowLog
        fields = '__all__'
        # depth = 3


class DealTicketSerializer(serializers.Serializer):
    transition_id = serializers.IntegerField(write_only=True)
    suggestion = serializers.CharField(write_only=True)

    def to_representation(self, obj):
        return TicketRecord(obj).data


class FileUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)

    class Meta:
        model = TicketFile
        fields = '__all__'
