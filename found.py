import data
from data_handler import save_item

def add_found_item():
    print("\n--- Add Found Item ---")
    name = input("Enter Item Name: ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")
    date_found = input("Enter Date Found (YYYY-MM-DD): ")
    location = input("Enter Location Found: ")

    item = {
        "id": data.item_counter,
        "name": name,
        "category": category,
        "description": description,
        "date": date_found,
        "location": location,
        "status": "Found"
    }

    data.found_items.append(item)
    save_item(item)

    print("✅ Found item added successfully!")
    data.item_counter += 1