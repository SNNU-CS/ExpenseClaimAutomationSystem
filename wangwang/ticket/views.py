from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.service import CONSTANT_SERVICE
from workflow.models import Transition
from workflow.serializers import StateSerializer, TransitionSerializer

from .models import TicketFlowLog, TicketRecord
from .serializers import DealTicketSerializer, TicketFlowLogSerializer, TicketRecordSerializer, CreateTicketRecordSerializer


class TicketView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'options']
    queryset = TicketRecord.objects.filter(is_deleted=False)
    serializer_class = TicketRecordSerializer

    def get_serializer_class(self):
        if self.action == 'deal_ticket':
            return DealTicketSerializer
        elif self.action == 'create':
            return CreateTicketRecordSerializer
        return super().get_serializer_class()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['creator'] = request.user
        username = request.user.username
        ticket_data = serializer.validated_data.pop('ticket_data')
        serializer.validated_data['participant'] = serializer.validated_data.get('participant', username)
        obj = serializer.save()
        TicketFlowLog.objects.create(
            ticket=obj,
            participant_type=obj.participant_type,
            participant=obj.participant,
            state=obj.state,
            ticket_data=ticket_data,
            creator=request.user
        )
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="transitions")
    def get_transitions(self, request, pk=None):
        ticket = self.get_object()
        queryset = Transition.objects.filter(source_state=ticket.state, is_deleted=False)
        ret = TransitionSerializer(queryset, many=True).data
        return Response(ret)

    @action(detail=True, methods=['post'], url_path="deal")
    def deal_ticket(self, request, pk=None):
        ticket = self.get_object()
        serializer = DealTicketSerializer(data=request.data)
        if not serializer.is_valid():
            from utils.exceptions import ValidationError
            raise ValidationError
        transition = Transition.objects.get(pk=serializer.validated_data['transition_id'])
        destination_state = transition.destination_state
        # update ticket
        ticket.state = destination_state
        if destination_state.type == CONSTANT_SERVICE.STATE_TYPE_END:
            ticket.is_end = True
        ticket.save()
        ticket_data = ''  # Todo
        TicketFlowLog.objects.create(
            ticket=ticket,
            transition=transition,
            suggestion=serializer.validated_data['suggestion'],
            state=destination_state,
            ticket_data=ticket_data
        )

    @action(detail=True, methods=['get'], url_path="flowlogs")
    def get_flowlogs(self, request, pk=None):
        ticket = self.get_object()
        queryset = TicketFlowLog.objects.filter(ticket=ticket, is_deleted=False).order_by('-id')
        ret = TicketFlowLogSerializer(queryset, many=True).data
        return Response(ret)

    @action(detail=True, methods=['get'], url_path="state")
    def get_state(self, request, pk=None):
        ticket = self.get_object()
        ret = StateSerializer(ticket.state).data
        return Response(ret)
