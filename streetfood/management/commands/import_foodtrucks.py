import csv
from django.core.management.base import BaseCommand
from streetfood.models import FoodTruck
from django.utils.dateparse import parse_datetime
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone


def parse_date(date_str):
    if not date_str:
        return None

    date_formats = [
        "%m/%d/%Y %I:%M:%S %p",  # Format: 'MM/DD/YYYY HH:MM:SS AM/PM'
        "%m/%d/%Y",  # Format: 'MM/DD/YYYY'
    ]

    for date_format in date_formats:
        try:
            return datetime.strptime(date_str, date_format).date()
        except ValueError:
            continue

    return None


class Command(BaseCommand):
    help = "Load a list of food trucks from a CSV file into the database"

    def add_arguments(self, parser):
        parser.add_argument("filename", type=str, help="The CSV file to load")

    def handle(self, *args, **options):
        # Open the CSV file
        with open(options["filename"], "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            # Create a FoodTruck object for each row and save it to the database
            for row in reader:
                noisent_value = float(row["NOISent"]) if row["NOISent"] else None
                dayshours = row["dayshours"]

                received_date_str = row["Received"]
                received_datetime = parse_datetime(received_date_str)

                # If the datetime is naive, make it timezone-aware
                if received_datetime and timezone.is_naive(received_datetime):
                    default_timezone = timezone.get_default_timezone()
                    received_datetime = timezone.make_aware(
                        received_datetime, default_timezone
                    )
                location_description = (
                    row["LocationDescription"].strip()
                    if "LocationDescription" in row
                    else ""
                )
                blocklot = row["blocklot"].strip() if "blocklot" in row else ""
                block = row["block"].strip() if "block" in row else ""
                lot = row["lot"].strip() if "lot" in row else ""
                fooditems = row["FoodItems"].strip() if "FoodItems" in row else ""

                # if not all([location_description, blocklot, block, lot, fooditems]):
                #     self.stdout.write(self.style.ERROR(f"Missing required field(s) for food truck: {row}"))
                #     continue

                facility_type = (
                    row["FacilityType"] if row["FacilityType"].strip() else None
                )
                approved_date = (
                    parse_date(row["Approved"]) if row["Approved"].strip() else None
                )
                expiration_date = (
                    parse_date(row["ExpirationDate"])
                    if row["ExpirationDate"].strip()
                    else None
                )
                x_value = float(row["X"]) if row["X"].strip() else None
                y_value = float(row["Y"]) if row["Y"].strip() else None
                fire_prevention_districts_value = (
                    int(row["Fire Prevention Districts"])
                    if row["Fire Prevention Districts"].strip()
                    else None
                )
                police_districts_value = (
                    int(row["Police Districts"])
                    if row["Police Districts"].strip()
                    else None
                )
                supervisor_districts_value = (
                    int(row["Supervisor Districts"])
                    if row["Supervisor Districts"].strip()
                    else None
                )
                zip_codes_value = (
                    int(row["Zip Codes"]) if row["Zip Codes"].strip() else None
                )
                neighborhoods_old_value = (
                    int(row["Neighborhoods (old)"])
                    if row["Neighborhoods (old)"].strip()
                    else None
                )

                food_truck = FoodTruck(
                    applicant=row["Applicant"],
                    address=row["Address"],
                    latitude=float(row["Latitude"]),
                    longitude=float(row["Longitude"]),
                    locationid=row["locationid"],
                    facility_type=facility_type,
                    cnn=row["cnn"],
                    location_description=location_description,
                    blocklot=blocklot,
                    block=block,
                    lot=lot,
                    fooditems=fooditems,
                    permit=row["permit"],
                    status=row["Status"],
                    x=x_value,
                    y=y_value,
                    fire_prevention_districts=fire_prevention_districts_value,
                    police_districts=police_districts_value,
                    supervisor_districts=supervisor_districts_value,
                    zip_codes=zip_codes_value,
                    neighborhoods_old=neighborhoods_old_value,
                    schedule=row["Schedule"],
                    dayshours=dayshours,
                    noisent=noisent_value,
                    approved=approved_date,
                    received=received_datetime,
                    prior_permit=row["PriorPermit"],
                    expiration_date=expiration_date,
                    location_point=row["Location"],
                )
                try:
                    food_truck.full_clean()  # Validate the model instance
                    food_truck.save()
                except ValidationError as e:
                    self.stdout.write(
                        self.style.ERROR(f"Failed to validate food truck: {e}")
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f"Failed to save food truck: {e}")
                    )

            self.stdout.write(self.style.SUCCESS("Successfully loaded food trucks"))
