# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as gismodels


class TimeStamp(models.Model):
    stamp = models.DateTimeField()
    # TODO, interval

    def __unicode__(self):
        return u'TimeStamp: %s' % self.stamp


class Location(models.Model):
    name = models.TextField()
    point = gismodels.PointField()

    def __unicode__(self):
        return u'Location: %s' % self.name


class EventType(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return u'EventType: %s' % self.name
    

class Event(models.Model):
    timestamp = models.ForeignKey(TimeStamp)
    location = models.ForeignKey(Location)
    eventtype = models.ForeignKey(EventType)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return u'Event: %s' % self.title
