from app import db
from __init__ import create_app
from models import Company
import csv
from datetime import datetime

def update_schema():
    with create_app().app_context():
        db.engine.execute('ALTER TABLE company ADD COLUMN founded_date DATE;')

def seed_data():
    # Example: Add some initial data
    with create_app.app_context():
        companies = [
            Company(name="TechCorp", category="Technology", subcategory="Software"),
            Company(name="GreenEnergy", category="Energy", subcategory="Renewable")
        ]
        db.session.add_all(companies)
        db.session.commit()

def import_from_csv(filename):
    # Example: Import data from a CSV file
    with create_app().app_context():
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                company = Company(name=row['name'], category=row['category'], subcategory=row['subcategory'])
                db.session.add(company)
        db.session.commit()

def cleanup_old_data():
    # Example: Remove companies older than a certain date
    with create_app().app_context():
        some_date = datetime(2000, 1, 1)
        Company.query.filter(Company.created_date < some_date).delete()
        db.session.commit()

def delete_all_data():
    # Example: Remove all data from the table
    with create_app().app_context():
        Company.query.delete()
        db.session.commit()

if __name__ == "__main__":
    update_schema()
    seed_data()
    import_from_csv('new_companies.csv')
    cleanup_old_data()
    print("Database update completed.")