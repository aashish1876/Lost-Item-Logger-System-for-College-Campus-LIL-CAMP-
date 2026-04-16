def view_items(items_list):
    if not items_list:
        print("⚠ No records available.")
        return

    for item in items_list:
        print("\nID:", item["id"])
        print("Name:", item["name"])
        print("Category:", item["category"])
        print("Description:", item["description"])
        print("Date:", item["date"])
        print("Location:", item["location"])
        print("Status:", item["status"])