# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Event, Location, EventType, TimeStamp


# Register your models here.
admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(Location)
admin.site.register(TimeStamp)
