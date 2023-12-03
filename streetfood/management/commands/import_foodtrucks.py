import csv
from django.core.management.base import BaseCommand
from streetfood.models import FoodTruck
from django.utils.dateparse import parse_datetime
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone

# Define a function to parse dates from strings in various formats.
def parse_date(date_str):
    # Return None if the date string is empty.
    if not date_str:
        return None

    # List of date formats to try parsing the date string.
    date_formats = [
        "%m/%d/%Y %I:%M:%S %p",  # Format: 'MM/DD/YYYY HH:MM:SS AM/PM'
        "%m/%d/%Y",  # Format: 'MM/DD/YYYY'
    ]

    # Try each date format and return the date if parsing is successful.
    for date_format in date_formats:
        try:
            return datetime.strptime(date_str, date_format).date()
        except ValueError:
            continue  # If parsing fails, try the next format.

    # Return None if none of the formats work.
    return None

# Define a Django management command to import food trucks from a CSV file.
class Command(BaseCommand):
    help = "Load a list of food trucks from a CSV file into the database"

    # Add a command-line argument for the CSV file name.
    def add_arguments(self, parser):
        parser.add_argument("filename", type=str, help="The CSV file to load")

    # The main method called when the command is run.
    def handle(self, *args, **options):
        # Open the CSV file specified by the command-line argument.
        with open(options["filename"], "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            # Iterate over each row in the CSV file.
            for row in reader:
                # Parse and clean up the data from the CSV file.
                noisent_value = float(row["NOISent"]) if row["NOISent"] else None
                dayshours = row["dayshours"]

                # Parse the 'Received' date using Django's parse_datetime utility.
                received_date_str = row["Received"]
                received_datetime = parse_datetime(received_date_str)

                # Make the datetime timezone-aware if it's naive.
                if received_datetime and timezone.is_naive(received_datetime):
                    default_timezone = timezone.get_default_timezone()
                    received_datetime = timezone.make_aware(received_datetime, default_timezone)

                # Strip whitespace from string fields to avoid validation errors.
                location_description = row["LocationDescription"].strip() if "LocationDescription" in row else ""
                blocklot = row["blocklot"].strip() if "blocklot" in row else ""
                block = row["block"].strip() if "block" in row else ""
                lot = row["lot"].strip() if "lot" in row else ""
                fooditems = row["FoodItems"].strip() if "FoodItems" in row else ""

                # Parse other fields, providing default values if they are missing or empty.
                facility_type = row["FacilityType"].strip() if row["FacilityType"].strip() else None
                approved_date = parse_date(row["Approved"].strip()) if row["Approved"].strip() else None
                expiration_date = parse_date(row["ExpirationDate"].strip()) if row["ExpirationDate"].strip() else None
                x_value = float(row["X"].strip()) if row["X"].strip() else None
                y_value = float(row["Y"].strip()) if row["Y"].strip() else None
                # ... (parsing other fields)

                # Create a FoodTruck instance with the parsed data.
                food_truck = FoodTruck(
                    # ... (assigning parsed data to model fields)
                )

                # Attempt to save the FoodTruck instance to the database.
                try:
                    food_truck.full_clean()  # Validate the model instance
                    food_truck.save()  # Save the instance
                except ValidationError as e:
                    # Handle validation errors by printing an error message.
                    self.stdout.write(self.style.ERROR(f"Failed to validate food truck: {e}"))
                except Exception as e:
                    # Handle other exceptions by printing an error message.
                    self.stdout.write(self.style.ERROR(f"Failed to save food truck: {e}"))

            # Print a success message after all records have been processed.
            self.stdout.write(self.style.SUCCESS("Successfully loaded food trucks"))
