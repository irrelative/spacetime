# SpaceTime DB

A fact table of time and space. Initially to be populated with wikipedia data.

Some sort of queries that could be fun:
 - Who was born near my current location?
 - What happened on my birthday?
 - Timeline of events for a location

Now in django

## Tables

*Event*

* id
* timestamp_id
* location_id
* event_type_id


*Timestamp*

* id
* timestamp (indexed?)
* duration (interval)


*Location*

* id
* shape (?)
* granularity (


*EventType*

* id
* name (birth, death, battle, etc)
