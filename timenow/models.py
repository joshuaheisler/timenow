from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class UserExtended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=300, null=True)
    date_created = models.DateTimeField(default=datetime.now)
    date_changed = models.DateTimeField(default=datetime.now)
    date_deleted = models.DateTimeField(null=True)


class UserContract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weekly_working_hours = models.IntegerField()
    vacation_days = models.IntegerField()
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    date_created = models.DateTimeField(default=datetime.now)
    date_changed = models.DateTimeField(default=datetime.now)


class UserRepresent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user')
    represent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_represent')
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    date_created = models.DateTimeField(default=datetime.now)
    date_changed = models.DateTimeField(default=datetime.now)
    date_deleted = models.DateTimeField(null=True)
