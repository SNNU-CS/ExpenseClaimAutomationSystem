from rest_framework import serializers

from workflow.serializers import StateSerializer, TransitionSerializer, WorkflowSerializer

from .models import TicketFlowLog, TicketRecord


class TicketRecordSerializer(serializers.ModelSerializer):
    workflow = WorkflowSerializer()
    state = StateSerializer()

    class Meta:
        model = TicketRecord
        fields = '__all__'


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
