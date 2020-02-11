from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.exceptions import InitStateNotConfig
from utils.service import CONSTANT_SERVICE

from .models import CustomField, State, Transition, Workflow
from .serializers import (
    CreateWorkflowSerializer, CustomFieldSerializer, StateSerializer, TransitionSerializer, WorkflowSerializer
)


class WorkflowView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'options']
    serializer_class = WorkflowSerializer
    queryset = Workflow.objects.filter(is_deleted=False).order_by('id')

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateWorkflowSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=['get'], url_path="init_state")
    def get_init_state(self, request, pk=None):
        workflow = self.get_object()
        init_state_obj = State.objects.filter(
            workflow=workflow, is_deleted=False, state_type=CONSTANT_SERVICE.STATE_TYPE_START
        ).first()
        if not init_state_obj:
            raise InitStateNotConfig
        transition_queryset = Transition.objects.filter(is_deleted=False, source_state=init_state_obj).all()
        transition_info_list = [
            dict(transition_id=transition.id, transition_name=transition.name) for transition in transition_queryset
        ]
        custom_field_queryset = CustomField.objects.filter(workflow=pk, is_deleted=False).order_by('order')
        field_list = CustomFieldSerializer(custom_field_queryset, many=True).data
        ret = StateSerializer(init_state_obj).data
        ret.update(field_list=field_list, transition=transition_info_list)
        return Response(ret)

    @action(detail=True, methods=['get'], url_path="states")
    def get_states(self, request, pk=None):
        workflow = self.get_object()
        states_queryset = State.objects.filter(is_deleted=False, workflow=workflow)
        ret = StateSerializer(states_queryset, many=True).data
        return Response(ret)

    @action(detail=True, methods=['get'], url_path="transitions")
    def get_transitions(self, request, pk=None):
        workflow = self.get_object()
        queryset = Transition.objects.filter(workflow=workflow, is_deleted=False)
        ret = TransitionSerializer(queryset, many=True).data
        return Response(ret)

    @action(detail=True, methods=['get'], url_path="custom_fields")
    def get_custom_fields(self, request, pk=None):
        workflow = self.get_object()
        queryset = CustomField.objects.filter(workflow=workflow, is_deleted=False)
        ret = CustomFieldSerializer(queryset, many=True).data
        return Response(ret)


class StateView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'options']
    serializer_class = StateSerializer
    queryset = State.objects.filter(is_deleted=False).order_by('id')

    def get_serializer_class(self):
        return super().get_serializer_class()


class TransitionView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'options']
    serializer_class = TransitionSerializer
    queryset = Transition.objects.filter(is_deleted=False).order_by('id')

    def get_serializer_class(self):
        return super().get_serializer_class()


class CustomFieldView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'options']
    serializer_class = CustomFieldSerializer
    queryset = CustomField.objects.filter(is_deleted=False).order_by('id')

    def get_serializer_class(self):
        return super().get_serializer_class()
