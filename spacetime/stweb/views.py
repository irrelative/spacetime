# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.list import ListView
from .models import Event

class EventListView(ListView):

    model = Event

    def get_context_data(self, **kwargs):
        data = super(EventListView, self).get_context_data(**kwargs)
        return data
