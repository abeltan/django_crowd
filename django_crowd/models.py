__author__ = 'abel'
from django.db import models

class Surveyee(models.Manager):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return Surveyee.name