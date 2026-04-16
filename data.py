from data_handler import load_data, initialize_file

initialize_file()
all_items = load_data()

lost_items = [item for item in all_items if item["status"] == "Lost"]
found_items = [item for item in all_items if item["status"] == "Found"]

item_counter = max([item["id"] for item in all_items], default=0) + 1