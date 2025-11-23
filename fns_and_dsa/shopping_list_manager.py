# shopping_list_manager.py
# Simple shopping list manager using Python lists.

def display_menu():
    print("\nShopping List Manager")           # <- plain print
    print("1. Add Item")                     # <- plain print
    print("2. Remove Item")                  # <- plain print
    print("3. View List")                    # <- plain print
    print("4. Exit")                         # <- plain print

def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print("'" + item + "' has been added to your shopping list.")  # <- plain print
    else:
        print("No item entered. Nothing was added.")  # <- plain print

def remove_item(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty. Nothing to remove.")  # <- plain print
        return

    item = input("Enter the item to remove: ").strip()
    if not item:
        print("No item entered. Nothing was removed.")  # <- plain print
        return

    # Exact match (case-sensitive)
    if item in shopping_list:
        shopping_list.remove(item)
        print("'" + item + "' has been removed from your shopping list.")  # <- plain print
        return

    # Case-insensitive match fallback
    lowered = [s.lower() for s in shopping_list]
    if item.lower() in lowered:
        index = lowered.index(item.lower())
        removed = shopping_list.pop(index)
        print(f"'{removed}' has been removed from your shopping list (case-insensitive match).")  # <- plain print
        return

    # Not found: show message and offer options
    print(f"'{item}' was not found in your shopping list.")  # <- plain print
    show = input("Would you like to see the current list? (y/n): ").strip().lower()
    if show == "y":
        view_list(shopping_list)  # uses print inside view_list
        try:
            idx = input("Enter the number of the item to remove (or press Enter to cancel): ").strip()
            if idx:
                idx = int(idx) - 1
                if 0 <= idx < len(shopping_list):
                    removed = shopping_list.pop(idx)
                    print("'" + removed + "' has been removed from your shopping list.")  # <- plain print
                else:
                    print("Index out of range. No item removed.")  # <- plain print
        except ValueError:
            print("Invalid number entered. No item removed.")  # <- plain print

def view_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty.")  # <- plain print
        return

    print("\nYour Shopping List:")  # <- plain print
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i}. {item}")  # <- plain print

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")  # <- plain print
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")  # <- plain print

if __name__ == "__main__":
    main()
