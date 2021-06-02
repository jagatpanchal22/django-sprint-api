# Generated by Django 3.2.3 on 2021-06-01 10:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprint',
            name='end',
        ),
        migrations.AddField(
            model_name='sprint',
            name='end_date',
            field=models.DateField(default=datetime.date(2021, 6, 1), unique=True),
        ),
        migrations.AddField(
            model_name='sprint',
            name='start_date',
            field=models.DateField(default=datetime.date(2021, 6, 1), unique=True),
        ),
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_assigned_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
