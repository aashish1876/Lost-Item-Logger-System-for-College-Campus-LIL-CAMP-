import data

def search_item():
    keyword = input("\nEnter item name to search: ").lower()
    found = False

    for item in data.lost_items + data.found_items:
        if keyword in item["name"].lower():
            print("\n🔎 Item Found:")
            print("ID:", item["id"])
            print("Name:", item["name"])
            print("Category:", item["category"])
            print("Status:", item["status"])
            found = True

    if not found:
        print("❌ No matching item found.")