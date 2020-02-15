from rest_framework import serializers

from utils.exceptions import WorkflowDoesNoeExist

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


class AddWorkflowStateSerializer(serializers.ModelSerializer):
    workflow = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = State
        exclude = ('creator', )

    def validate_workflow(self, value):

        obj = Workflow.objects.filter(pk=value).first()
        if not obj:
            raise WorkflowDoesNoeExist
        return obj

    def to_representation(self, obj):
        return StateSerializer(obj).data


class StateSerializer(serializers.ModelSerializer):
    state_type = serializers.CharField(read_only=True, source='get_state_type_display')
    participant_type = serializers.CharField(read_only=True, source='get_participant_type_display')
    distribute_type = serializers.CharField(read_only=True, source='get_distribute_type_display')
    creator = serializers.SerializerMethodField(read_only=True)
    workflow = serializers.CharField(read_only=True, source='workflow.name')

    def get_creator(self, obj):
        return obj.creator.username if obj.creator else '--'

    class Meta:
        model = State
        fields = '__all__'


class CustomFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomField
        fields = '__all__'


class CustomFieldDetailSerializer(serializers.ModelSerializer):
    workflow = serializers.CharField(source='workflow.name', read_only=True)
    sub_workflow = serializers.CharField(source='sub_workflow.name', read_only=True)
    field_type = serializers.CharField(source="get_field_type_display", read_only=True)
    creator = serializers.CharField(read_only=True, source="creator.username")

    class Meta:
        model = CustomField
        fields = '__all__'


class TransitionSerializer(serializers.ModelSerializer):
    source_state = StateSerializer(read_only=True)
    destination_state = StateSerializer(read_only=True)
    attribute_type = serializers.CharField(source='get_attribute_type_display', read_only=True)
    transition_type = serializers.CharField(source="get_transition_type_display", read_only=True)
    workflow = serializers.CharField(source='workflow.name', read_only=True)
    creator = serializers.CharField(read_only=True, source="creator.username")

    class Meta:
        model = Transition
        fields = '__all__'
