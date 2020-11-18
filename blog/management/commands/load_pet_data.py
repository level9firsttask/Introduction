from csv import DictReader
import csv
from datetime import datetime

from django.core.management import BaseCommand

from blog.models import Airport
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

l = []

with open('new_airport.csv', 'r') as read_file:
    reader = csv.reader(read_file)
    next(reader)
    row = list(reader)
    for i in row:
        if len(i) != 0 :
            l.append(i[0])

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from new_airport.csv into our Pet mode"

    def handle(self, *args, **options):
        if Airport.objects.exists():
            print('Airport data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Creating vaccine data")
       
        print("Loading Airport data")
        for row in DictReader(open('./new_airport.csv')):
            airport = Airport()
            airport.iata = row['iata']
            airport.icao = row['icao']
            airport.airport_name = row['airport_name']
            airport.location= row['location']
            airport.gps= row['gps']
            
            
            airport.save()
