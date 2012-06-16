from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class AccountAccess(models.Model):
    "Authorized remote service."

    identifier = models.CharField(max_length=255)
    service = models.CharField(max_length=50)
    user = models.ForeignKey('auth.User', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, default=datetime.now)
    modified = models.DateTimeField(auto_now=True, default=datetime.now)    
    access_token = models.TextField(default='', blank=True)
    raw_data = models.TextField(default='', blank=True)

    class Meta(object):
        unique_together = ('identifier', 'service')
