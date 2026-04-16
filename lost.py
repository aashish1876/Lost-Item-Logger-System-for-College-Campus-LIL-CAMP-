import data
from data_handler import save_item

def add_lost_item():
    print("\n--- Add Lost Item ---")
    name = input("Enter Item Name: ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")
    date_lost = input("Enter Date Lost (YYYY-MM-DD): ")
    location = input("Enter Location Lost: ")

    item = {
        "id": data.item_counter,
        "name": name,
        "category": category,
        "description": description,
        "date": date_lost,
        "location": location,
        "status": "Lost"
    }

    data.lost_items.append(item)
    save_item(item)

    print("✅ Lost item added successfully!")
    data.item_counter += 1