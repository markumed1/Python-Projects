from datetime import datetime
from pytz import timezone
import pytz

portland_time = datetime.now(tz=pytz.UTC).replace(microsecond=0)
Portland = portland_time.astimezone(pytz.timezone('US/Pacific'))

new_york_time = portland_time.astimezone(timezone('US/Eastern'))
Ny = new_york_time

london_time = portland_time.astimezone(timezone('Europe/London'))
London = london_time

cities = {'Portland': Portland, 
          'Ny': Ny, 
          'London': London}

for city in cities:
    Branchtime=int(cities[city].strftime('%H'))
    if Branchtime >= 9 and Branchtime < 21:
        print(city, cities[city], 'OPEN')
    else:
        print(city, cities[city], 'CLOSED')
