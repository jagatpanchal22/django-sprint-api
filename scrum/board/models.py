import datetime
from django.utils.timezone import now
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Sprint(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    start_date = models.DateField(unique=True, default=now)
    end_date = models.DateField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name or _('Sprint ending %s') % self.end_date


class Task(models.Model):
    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = [
                         (STATUS_TODO, _("Not Started")),
                         (STATUS_IN_PROGRESS, _("In Progress")),
                         (STATUS_TESTING, _("In Testing")),
                         (STATUS_DONE, _("Done"))
                     ],

    STATUS_CHOICES = [
        ("1", _("Not Started")),
        ("2", _("In Progress")),
        ("3",  _("In Testing")),
        ("4", _("Done")),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, blank=True, null=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_TODO)
    order = models.SmallIntegerField(default=0)
    created = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='task_created_by', on_delete=models.SET_NULL, null=True, blank=True)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='task_assigned_to', on_delete=models.SET_NULL, null=True, blank=True)
    started = models.DateField(blank=True, null=True)
    due = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
