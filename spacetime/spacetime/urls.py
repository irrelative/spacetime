"""spacetime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from stweb import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^event/new', views.EventCreate.as_view(), name='event-create'),
    url(r'^event/(?P<pk>\d+)/edit', views.EventUpdate.as_view(), name='event-update'),
    url(r'^event/(?P<pk>\d+)', views.EventDetail.as_view(), name='event-detail'),
    url(r'^location-autocomplete', views.LocationAutocomplete.as_view(), name='location-autocomplete'),
    url(r'^timestamp-autocomplete', views.TimeStampAutocomplete.as_view(), name='timestamp-autocomplete'),
    url(r'^eventtype-autocomplete', views.EventTypeAutocomplete.as_view(), name='eventtype-autocomplete'),
    url(r'^', views.EventListView.as_view(), name='event-list'),
]
