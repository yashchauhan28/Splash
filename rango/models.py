from __future__ import unicode_literals

from django.db import models

class UserInformation(models.Model):
    name = models.CharField(max_length=128)
    uniqueid = models.CharField(primary_key=True,max_length=120) #name for user -- not given to specific app
    email = models.CharField(max_length=120)
    email_password = models.CharField(max_length=120)
    fbOath = models.CharField(max_length=120)

    def __unicode__(self):
        return unicode(self.uniqueid)

class ConnectionDetail(models.Model):
    uniqueid = models.ForeignKey(UserInformation)
    pc = models.CharField(max_length=120)
    app = models.CharField(max_length=120)

    def __unicode__(self):
        return unicode(self.uniqueid)
