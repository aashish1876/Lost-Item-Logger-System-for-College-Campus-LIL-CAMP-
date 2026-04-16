import csv
import os

FILE_NAME = "items.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name", "category", "description", "date", "location", "status"])

def load_data():
    items = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["id"] = int(row["id"])
                items.append(row)
    return items

def save_item(item):
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            item["id"],
            item["name"],
            item["category"],
            item["description"],
            item["date"],
            item["location"],
            item["status"]
        ])

def rewrite_csv(all_items):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id","name","category","description","date","location","status"])
        writer.writeheader()
        for item in all_items:
            writer.writerow(item)