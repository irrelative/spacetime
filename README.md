# SpaceTime DB

A fact table of time and space. Initially to be populated with wikipedia data.

Some sort of queries that could be fun:
 - Who was born near my current location?
 - What happened on my birthday?
 - Timeline of events for a location

Now in django

## Timestamp assumptions
* Min/Max follows python/db constraits. Eg: minimum year is 1CE from https://docs.python.org/3/library/datetime.html .
  Will consider other values as things progress. eg: postgres minimum ts is 4713 BC.

## Location assumptions
* Only on earth

