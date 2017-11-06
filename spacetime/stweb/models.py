# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TimeStamp(models.Model):
    stamp = models.DateTimeField()
    # TODO, interval


class Location(models.Model):
    name = models.TextField()


class EventType(models.Model):
    name = models.TextField()
    

class Event(models.Model):
    timestamp = models.ForeignKey(TimeStamp)
    location = models.ForeignKey(Location)
    eventtype = models.ForeignKey(EventType)
    title = models.TextField()
    description = models.TextField()

