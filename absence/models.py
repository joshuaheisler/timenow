from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Absence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user', verbose_name='Benutzer', default=None)
    comment = models.CharField(max_length=300, default=None, verbose_name='Kommentar')
    absence_from = models.DateField(verbose_name='Abwesend von')
    absence_to = models.DateField(verbose_name='Abwesend bis')
    approved = models.BooleanField(default=None, verbose_name='Genehmigt', null=True)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_approver', verbose_name='Genehmiger', null=True)
    approved_at = models.DateTimeField(default=datetime.now, verbose_name='Genehmigt am', null=True)
    approved_by_comment = models.CharField(max_length=300, default=None, verbose_name='Kommentar des Genehmigers')

    @property
    def amount_of_days(self):
        """Returns the amount of days of the absence"""
        return abs((self.absence_to - self.absence_from).days) + 1
