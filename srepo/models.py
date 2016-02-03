from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=20)
    ID = models.CharField(max_length=3, 
        primary_key=True, 
        validators=[
        RegexValidator(
            regex='^[a-z|0-9]{3}$',
            message='3 characters ID in lower case',
            )],
        )

    def __str__(self):
        return self.ID

class Build(models.Model):
    application = models.ForeignKey(Application, related_name='builds')
    created = models.DateTimeField(auto_now_add=True)
    branch = models.CharField(max_length=200)
    commitId = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return '%s-%s' % (self.id, self.application)
    class Meta:
        ordering = ['-created']
