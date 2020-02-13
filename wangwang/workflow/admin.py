from django.contrib import admin

from .models import CustomField, State, Transition, Workflow

base_list_display = ('creator', 'created', 'modified')


class WorkflowAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('id', 'name', 'description') + base_list_display


class StateAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = (
        'id',
        'name',
        'order',
        'state_type',
        'workflow',
        'sub_workflow',
    ) + base_list_display


class TransitionAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = (
        'id',
        'name',
        'workflow',
        'transition_type',
        'source_state',
        'destination_state',
    ) + base_list_display


class CustomFieldAdmin(admin.ModelAdmin):
    search_fields = ('workflow_id', )
    list_display = ('id', 'workflow', 'field_type', 'field_key', 'field_name', 'order', 'required') + base_list_display


# class WorkflowScriptAdmin(admin.ModelAdmin):
#     search_fields = ('name', )
#     list_display = ('id', 'name', 'description', 'is_active') + base_list_display

# class CustomNoticeAdmin(admin.ModelAdmin):
#     search_fields = ('name', )
#     list_display = ('name', 'description') + base_list_display

#     def formfield_for_dbfield(self, db_field, **kwargs):
#         field = super(CustomNoticeAdmin, self).formfield_for_dbfield(db_field, **kwargs)
#         if db_field.name == 'title_template':
#             field.initial = '你有一个待办工单:{title}'
#         if db_field.name == 'content_template':
#             field.initial = '标题:{title}, 创建时间:{gmt_created}'
#         return field

admin.site.register(Workflow, WorkflowAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Transition, TransitionAdmin)
admin.site.register(CustomField, CustomFieldAdmin)
# admin.site.register(WorkflowScript, WorkflowScriptAdmin)
