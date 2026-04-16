import data
from data_handler import rewrite_csv

def claim_item():
    try:
        item_id = int(input("\nEnter Item ID to claim: "))

        all_items = data.lost_items + data.found_items

        for item in all_items:
            if item["id"] == item_id and item["status"] == "Found":
                item["status"] = "Claimed"

                # update memory lists
                data.found_items[:] = [i for i in data.found_items if i["status"] == "Found"]

                # rewrite CSV
                rewrite_csv(all_items)

                print("✅ Item claimed successfully!")
                return

        print("❌ Item not found or already claimed.")

    except ValueError:
        print("Invalid ID entered.")