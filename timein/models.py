from __future__ import unicode_literals

import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile')

    @property
    def get_timelogs(self):
        return self.user.timelog.all()


class TimeRecord(models.Model):
    created  = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        today = datetime.datetime.today()

        if not self.id:
            if not self.created:
                self.created = today
            if not self.modified:
                self.modified = today
        else:
            self.modified = today

        super(TimeinRecords, self).save(*args, **kwargs)


class TimeLog(models.Model):
    owner = models.ForeignKey(User, related_name='timelog')
    time_in = models.ForeignKey(TimeRecord, null=True, blank=True, related_name='time_in')
    time_out = models.ForeignKey(TimeRecord, null=True, blank=True, related_name='time_out')
