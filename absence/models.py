from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Absence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user')
    comment = models.CharField(max_length=300, default=None)
    absence_from = models.DateField()
    absence_to = models.DateField()
    approved = models.BooleanField(default=None)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_approver')
    approved_at = models.DateTimeField(default=datetime.now)
    approved_by_comment = models.CharField(max_length=300, default=None)

    @property
    def amount_of_days(self):
        """Returns the amount of days of the absence"""
        return abs((self.absence_to - self.absence_from).days) + 1
