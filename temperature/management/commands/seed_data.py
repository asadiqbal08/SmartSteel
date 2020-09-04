from django.core.management.base import BaseCommand, CommandError
from temperature.models import Temperature
from django.utils.dateparse import parse_datetime

import pandas as pd


class Command(BaseCommand):
    """Transfers `task_data.csv` to a database"""

    help = "Creates or updates seed data based on a raw data CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            '--csvfile', 
            nargs='+', 
            type=str, 
            help="The CSV file that needs to dump into database", 
            required=True
        )

    def handle(self, *args, **options):

        # For the current problem, Code is expecting to dump data from 
        # given single .csv file that is provided along with assignment instead of multiples.
        csv_file = options['csvfile'][0]

        # Used pandas python lib to load CSV data into dataframes that will be well organized. 
        # ref: https://pypi.org/project/pandas/
        df = pd.read_csv (csv_file, sep=',')

        temperatures = [
            Temperature(
                uuid=row['id'],
                timestamp=parse_datetime(row['timestamp']),
                temperature=row['temperature'],
                duration=row['duration'],
            )
            for __, row in df.iterrows()
        ]

        try:
            Temperature.bulk_update_or_create(temperatures)
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(
                    'Failed to dump data from CSV to database: ' + str(e)
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    "Data dump successfully!"
                )
            )
