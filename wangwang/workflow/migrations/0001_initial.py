# Generated by Django 2.2.7 on 2020-02-13 10:36

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0004_auto_20200211_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('order', models.IntegerField(default=0, help_text='用于工单步骤接口时，step上状态的顺序(因为存在网状情况，所以需要人为设定顺序),值越小越靠前', verbose_name='状态顺序')),
                ('state_type', models.IntegerField(choices=[(0, '普通类型'), (1, '初始状态'), (2, '结束状态')], default=0, help_text='0.普通类型 1.初始状态(用于新建工单时,获取对应的字段必填及transition信息) 2.结束状态(此状态下的工单不得再处理，即没有对应的transition)', verbose_name='状态类型id')),
                ('participant_type', models.IntegerField(blank=True, choices=[(0, '无处理人'), (1, '个人'), (2, '多人'), (3, '部门'), (4, '角色'), (5, '脚本'), (6, '参与人')], default=1, help_text='0.无处理人,1.个人,2.多人,3.部门,4.角色,5.脚本,6.参与人', verbose_name='参与者类型')),
                ('participant', models.CharField(blank=True, default='', help_text='可以为空(无处理人的情况，如结束状态)、username、多个username(以,隔开)、部门id、角色id、脚本,机器人等', max_length=100, verbose_name='参与者')),
                ('creator', models.ForeignKey(help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User')),
            ],
            options={
                'verbose_name': '工作流状态',
                'verbose_name_plural': '工作流状态',
            },
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('description', models.CharField(max_length=50, verbose_name='描述')),
                ('flowchart', models.FileField(blank=True, help_text='工作流的流程图,为了方便别人', upload_to='flowchart', verbose_name='流程图')),
                ('creator', models.ForeignKey(help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User')),
            ],
            options={
                'verbose_name': '工作流',
                'verbose_name_plural': '工作流',
            },
        ),
        migrations.CreateModel(
            name='Transition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='操作')),
                ('transition_type', models.IntegerField(choices=[(0, '常规流转'), (1, '定时器流转')], default=0, help_text='0.常规流转，1.定时器流转,需要设置定时器时间', verbose_name='流转类型')),
                ('timer', models.IntegerField(default=0, help_text='流转类型设置为定时器流转时生效,单位秒。处于源状态X秒后如果状态都没有过变化则自动流转到目标状态', verbose_name='定时器(单位秒)')),
                ('condition_expression', models.CharField(default='[]', help_text='流转条件表达式，根据表达式中的条件来确定流转的下个状态', max_length=1000, verbose_name='条件表达式')),
                ('attribute_type', models.IntegerField(choices=[(0, '同意'), (1, '拒绝'), (2, '其他')], default=0, help_text='属性类型，0.同意，1.拒绝，2.其他', verbose_name='属性类型')),
                ('creator', models.ForeignKey(help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User')),
                ('destination_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_transitions', to='workflow.State', verbose_name='目的状态')),
                ('source_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_transitions', to='workflow.State', verbose_name='源状态')),
                ('workflow', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workflow_transitions', to='workflow.Workflow', verbose_name='工作流id')),
            ],
            options={
                'verbose_name': '工作流流转',
                'verbose_name_plural': '工作流流转',
            },
        ),
        migrations.AddField(
            model_name='state',
            name='sub_workflow',
            field=models.ForeignKey(blank=True, help_text='如果需要在此状态启用子工单,请填写对应的工作流id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_workflow_states', to='workflow.Workflow', verbose_name='子工作流'),
        ),
        migrations.AddField(
            model_name='state',
            name='workflow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workflow_states', to='workflow.Workflow', verbose_name='工作流'),
        ),
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('field_type', models.IntegerField(choices=[(0, '字符串'), (1, '整形'), (2, '布尔'), (3, '日期'), (4, '日期时间'), (5, '单选框'), (6, '多选框'), (7, '下拉列表'), (8, '多选下拉列表'), (9, '文本域'), (10, '附件'), (11, '用户'), (12, '多选用户')], help_text=[(0, '字符串'), (1, '整形'), (2, '布尔'), (3, '日期'), (4, '日期时间'), (5, '单选框'), (6, '多选框'), (7, '下拉列表'), (8, '多选下拉列表'), (9, '文本域'), (10, '附件'), (11, '用户'), (12, '多选用户')], verbose_name='类型')),
                ('field_key', models.CharField(help_text='字段类型请尽量特殊，避免与系统中关键字冲突', max_length=50, verbose_name='字段标识')),
                ('field_name', models.CharField(max_length=50, verbose_name='字段名称')),
                ('order', models.IntegerField(default=0, help_text='工单基础字段在表单中排序为:流水号-1,标题-2,状态-3,创建人-4,创建时间99,更新时间100.', verbose_name='排序')),
                ('default_value', models.CharField(blank=True, help_text='前端展示时，可以将此内容作为表单中的该字段的默认值', max_length=100, null=True, verbose_name='默认值')),
                ('description', models.CharField(blank=True, default='', help_text='字段的描述信息，可以将此内容作为placeholder', max_length=100, verbose_name='描述')),
                ('field_choice', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='radio,select类型可供选择的选项，格式为json如:[{"text":"","value":""}]', verbose_name='radio、checkbox、select的选项')),
                ('required', models.BooleanField(default=False, help_text='是否是必填项')),
                ('creator', models.ForeignKey(help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workflow_fields', to='workflow.Workflow', verbose_name='工作流')),
            ],
            options={
                'verbose_name': '工作流自定义字段',
                'verbose_name_plural': '工作流自定义字段',
            },
        ),
    ]
