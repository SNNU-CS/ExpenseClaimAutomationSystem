from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.exceptions import InitStateNotConfig

from .models import CustomField, State, Transition, Workflow
from .serializers import (
    AddWorkflowStateSerializer, CreateWorkflowSerializer, CustomFieldSerializer, StateSerializer, TransitionSerializer,
    WorkflowSerializer
)


class WorkflowView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'options']
    serializer_class = WorkflowSerializer
    queryset = Workflow.objects.order_by('id')

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateWorkflowSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=['get'], url_path="init_state")
    def get_init_state(self, request, pk=None):
        workflow = self.get_object()
        init_state = workflow.get_init_state()
        if not init_state:
            raise InitStateNotConfig
        custom_field_queryset = workflow.workflow_fields.order_by('order')
        field_list = CustomFieldSerializer(custom_field_queryset, many=True).data
        ret = StateSerializer(init_state).data
        ret.update(fields=field_list)
        return Response(ret)

    @action(detail=True, methods=['get'], url_path="states")
    def get_states(self, request, pk=None):
        workflow = self.get_object()
        states_queryset = workflow.workflow_states
        ret = StateSerializer(states_queryset, many=True).data
        return Response(ret)

    @action(detail=True, methods=['get'], url_path="transitions")
    def get_transitions(self, request, pk=None):
        workflow = self.get_object()
        queryset = workflow.workflow_transitions
        ret = TransitionSerializer(queryset, many=True).data
        return Response(ret)

    @action(detail=True, methods=['get'], url_path="fields")
    def get_custom_fields(self, request, pk=None):
        workflow = self.get_object()
        queryset = workflow.workflow_fields
        ret = CustomFieldSerializer(queryset, many=True).data
        return Response(ret)


class StateView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'options']
    serializer_class = StateSerializer
    queryset = State.objects.order_by('id')

    def get_serializer_class(self):
        if self.action == 'create':
            return AddWorkflowStateSerializer
        return super().get_serializer_class()

    def create(self, request):
        serializer = AddWorkflowStateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['creator'] = request.user
        serializer.save()
        return Response(serializer.data)


class TransitionView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'options']
    serializer_class = TransitionSerializer
    queryset = Transition.objects.order_by('id')

    def get_serializer_class(self):
        return super().get_serializer_class()


class CustomFieldView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'options']
    serializer_class = CustomFieldSerializer
    queryset = CustomField.objects.order_by('id')

    def get_serializer_class(self):
        return super().get_serializer_class()
