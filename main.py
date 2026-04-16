from lost import add_lost_item
from found import add_found_item
from view import view_items
from search import search_item
from claim import claim_item
import data

def main():
    while True:
        print("\n============================")
        print(" LIL-CAMP SYSTEM ")
        print("============================")
        print("1. Add Lost Item")
        print("2. Add Found Item")
        print("3. View Lost Items")
        print("4. View Found Items")
        print("5. Search Item")
        print("6. Claim Item")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_lost_item()
        elif choice == "2":
            add_found_item()
        elif choice == "3":
            view_items(data.lost_items)
        elif choice == "4":
            view_items(data.found_items)
        elif choice == "5":
            search_item()
        elif choice == "6":
            claim_item()
        elif choice == "7":
            print("Thank you for using LIL-CAMP 😊")
            break
        else:
            print("Invalid choice. Please try again.")

main()