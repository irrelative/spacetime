# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django import forms

from django.urls import reverse

from dal import autocomplete

from .models import Event, Location, TimeStamp, EventType
from .forms import EventForm

class EventListView(ListView):
    model = Event

    def get_context_data(self, **kwargs):
        data = super(EventListView, self).get_context_data(**kwargs)
        return data


class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    def get_success_url(self):
        return reverse('event-list')


class EventUpdate(UpdateView):
    model = Event
    form_class = EventForm
    def get_success_url(self):
        return reverse('event-list')


class EventDetail(DetailView):
    model = Event


class LocationAutocomplete(autocomplete.Select2QuerySetView):
    model = Location

class TimeStampAutocomplete(autocomplete.Select2QuerySetView):
    model = TimeStamp

class EventTypeAutocomplete(autocomplete.Select2QuerySetView):
    model = EventType
