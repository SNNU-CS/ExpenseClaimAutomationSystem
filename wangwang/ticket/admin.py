from django.contrib import admin

from ticket.models import TicketFlowLog, TicketRecord

base_list_display = ('creator', 'created', 'modified')


class TicketRecordAdmin(admin.ModelAdmin):
    search_fields = ('sn', 'title')
    list_display = (
        'id', 'sn', 'title', 'workflow', 'state', 'parent_ticket', 'participant_type', 'participant',
    ) + base_list_display


class TicketFlowLogAdmin(admin.ModelAdmin):
    search_fields = ('ticket', )
    list_display = ('id', 'ticket', 'transition', 'suggestion', 'participant_type', 'participant', 'state')


# class TicketCustomFieldAdmin(admin.ModelAdmin):
#     search_fields = ('name', )
#     list_display = ('id', 'ticket_id', 'name', 'field_key') + base_list_display

admin.site.register(TicketRecord, TicketRecordAdmin)
admin.site.register(TicketFlowLog, TicketFlowLogAdmin)
# admin.site.register(TicketCustomField, TicketCustomFieldAdmin)
