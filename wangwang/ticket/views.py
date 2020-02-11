from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.service import CONSTANT_SERVICE
from workflow.models import Transition
from workflow.serializers import StateSerializer, TransitionSerializer

from .models import TicketFlowLog, TicketRecord
from .serializers import DealTicketSerializer, TicketFlowLogSerializer, TicketRecordSerializer


class TicketView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'options']
    queryset = TicketRecord.objects.filter(is_deleted=False)
    serializer_class = TicketRecordSerializer

    def get_serializer_class(self):
        if self.action == 'deal_ticket':
            return DealTicketSerializer
        return super().get_serializer_class()

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
