from dal import autocomplete
from django import forms

from .models import Event, Location, TimeStamp, EventType


class EventForm(forms.ModelForm):
    timestamp = forms.ModelChoiceField(
        queryset=TimeStamp.objects.all(),
        widget=autocomplete.ModelSelect2(url='timestamp-autocomplete')
    )

    location = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        widget=autocomplete.ModelSelect2(url='location-autocomplete')
    )

    eventtype = forms.ModelChoiceField(
        queryset=EventType.objects.all(),
        widget=autocomplete.ModelSelect2(url='eventtype-autocomplete')
    )

    class Meta:
        model = Event
        fields = ('__all__')

