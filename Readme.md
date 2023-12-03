# Project Title
Food Truck Finder

## Description
Our team in San Francisco are on a quest to discover the hidden gems of street food, particularly food trucks.
The only requirement for the assignment is that  it gives us at least 5 food trucks to choose from a particular latitude and longitude.

## Getting Started

```bash
pip install django
pip install djangorestframework
```

### Dependencies
django, djangorestframework

### Executing program

```bash
python manage.py migrate
python manage.py import_foodtrucks ./data/food-truck-data.csv
python manage.py runserver
```

## Authors
Marin Markovic

## Built With

- Django - The web framework used
- PostgreSQL - Database

## Result

```bash
request:
    http://127.0.0.1:8000/api/foodtrucks?latitude=37.79092151&longitude=-122.4001004
    GET /api/foodtrucks?latitude=37.79092151&longitude=-122.4001004

response:
    {
        "food_trucks": [
            {
                "applicant": "MOMO INNOVATION LLC",
                "address": "1 BUSH ST",
                "fooditems": "Noodles",
                "latitude": 37.79092150726921,
                "longitude": -122.4001004237385,
                "locationid": "1733786",
                "facility_type": "Truck",
                "cnn": "3420000",
                "location_description": "BUSH ST: BATTERY ST to SANSOME ST (100 - 199)",
                "permit": "23MFF-00028",
                "status": "APPROVED",
                "dayshours": "",
                "approved": "2023-10-18",
                "expiration_date": "2024-11-15",
                "zip_codes": 28854,
                "neighborhoods_old": 6
            },
            {
                "applicant": "Roadside Rotisserie Corporation / Country Grill",
                "address": "1 BUSH ST",
                "fooditems": "Rotisserie Chicken: Ribs: Kickass Salad: Potatos w/fat dripping: chicken wrap.",
                "latitude": 37.79092150726921,
                "longitude": -122.4001004237385,
                "locationid": "1732700",
                "facility_type": "Truck",
                "cnn": "3419000",
                "location_description": "BUSH ST: 01ST ST \\ MARKET ST to BATTERY ST (1 - 99)",
                "permit": "23MFF-00021",
                "status": "REQUESTED",
                "dayshours": "",
                "approved": null,
                "expiration_date": "2024-11-15",
                "zip_codes": 28854,
                "neighborhoods_old": 6
            },
            {
                "applicant": "Off the Grid Services, LLC",
                "address": "1 BUSH ST",
                "fooditems": "",
                "latitude": 37.79092150726921,
                "longitude": -122.4001004237385,
                "locationid": "1416733",
                "facility_type": "Truck",
                "cnn": "11542000",
                "location_description": "SANSOME ST: SUTTER ST to BUSH ST (1 - 99)",
                "permit": "20MFF-00003",
                "status": "REQUESTED",
                "dayshours": "",
                "approved": null,
                "expiration_date": "2020-07-15",
                "zip_codes": 28854,
                "neighborhoods_old": 6
            },
            {
                "applicant": "Shah's Halal Food",
                "address": "532 MARKET ST",
                "fooditems": "Chicken Gyro: Lamb Gyro: Chiken Gyro Plate: Lamb Gyro Plate: Combination Gyro Plate.",
                "latitude": 37.79054831818324,
                "longitude": -122.40033367367877,
                "locationid": "1591832",
                "facility_type": "Push Cart",
                "cnn": "8742202",
                "location_description": "MARKET ST: BATTERY ST to SUTTER ST (540 - 558) -- NORTH --",
                "permit": "22MFF-00022",
                "status": "SUSPEND",
                "dayshours": "",
                "approved": null,
                "expiration_date": "2022-11-15",
                "zip_codes": 28854,
                "neighborhoods_old": 6
            },
            {
                "applicant": "Tacos Rodriguez",
                "address": "1 SANSOME ST",
                "fooditems": "Tacos: burritos: quesadillas: soda & water",
                "latitude": 37.790485146128,
                "longitude": -122.40094044068951,
                "locationid": "1591839",
                "facility_type": "Truck",
                "cnn": "11542000",
                "location_description": "SANSOME ST: SUTTER ST to BUSH ST (1 - 99)",
                "permit": "22MFF-00024",
                "status": "SUSPEND",
                "dayshours": "",
                "approved": null,
                "expiration_date": "2022-11-15",
                "zip_codes": 28854,
                "neighborhoods_old": 6
            }
        ]
    }
```

### Justify Framework Choices

- **Django**: Chosen for its "batteries-included" philosophy, Django offers a comprehensive standard library and components like an ORM for database interactions, an admin panel for easy management of data, and middleware support for extending request/response processing. It's also known for its robust security features, which are crucial for production-ready applications.
- **Django REST framework**:  It simplifies and accelerates API development

### Discuss Architecture

- **RESTful API**
- **Postgres**

### Improve Solution

- **NoSQL for Speed**
- **Third-party Services**
- **Performance Optimization**
- **Scalability Enhancements**
- **Testing and Security**
