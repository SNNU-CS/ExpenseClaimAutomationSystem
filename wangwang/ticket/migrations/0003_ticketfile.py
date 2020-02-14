# Generated by Django 2.2.7 on 2020-02-13 12:59

from django.db import migrations, models
import django.db.models.deletion
import ticket.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200211_1115'),
        ('ticket', '0002_auto_20200213_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to=ticket.models.file_upload_path)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('creator', models.ForeignKey(help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User')),
            ],
        ),
    ]