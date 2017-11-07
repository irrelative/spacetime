# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse

from .models import Event

class EventListView(ListView):
    model = Event

    def get_context_data(self, **kwargs):
        data = super(EventListView, self).get_context_data(**kwargs)
        return data


class EventCreate(CreateView):
    model = Event
    fields = ['timestamp', 'location', 'eventtype', 'title', 'description']
    def get_success_url(self):
        return reverse('event-list')
