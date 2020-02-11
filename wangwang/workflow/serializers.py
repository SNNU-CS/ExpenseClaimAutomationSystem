from rest_framework import serializers

from .models import CustomField, State, Transition, Workflow


class WorkflowSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField(read_only=True)

    def get_creator(self, obj):
        return obj.creator.username

    class Meta:
        model = Workflow
        fields = '__all__'


class CreateWorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workflow
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    state_type = serializers.CharField(read_only=True, source='get_state_type_display')
    participant_type = serializers.CharField(read_only=True, source='get_participant_type_display')
    distribute_type = serializers.CharField(read_only=True, source='get_distribute_type_display')
    creator = serializers.SerializerMethodField(read_only=True)

    def get_creator(self, obj):
        return obj.creator.username

    class Meta:
        model = State
        fields = '__all__'


class CustomFieldSerializer(serializers.ModelSerializer):
    field_type = serializers.CharField(read_only=True, source='get_field_type_display')

    class Meta:
        model = CustomField
        fields = '__all__'


class TransitionSerializer(serializers.ModelSerializer):
    source_state = StateSerializer()
    destination_state = StateSerializer()

    class Meta:
        model = Transition
        fields = '__all__'
