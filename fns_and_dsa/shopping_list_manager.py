def display_menu():
    print("\n🛒 Shopping List Manager")
    print("--------------------------")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View current list")
    print("4. Exit")

def main():
    shopping_list = []
    print("👋 Welcome to your Personal Shopping List Manager!")

    while True:
        display_menu()
        choice = input("👉 Choose an option (1-4): ").strip()

        if choice == '1':
            item = input("🔹 What would you like to add? ").strip()
            if item:
                shopping_list.append(item)
                print(f"✅ '{item}' added to your list.")
            else:
                print("⚠️ You didn't enter any item. Please try again.")

        elif choice == '2':
            item = input("🔻 What would you like to remove? ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"🗑️ '{item}' removed from your list.")
            else:
                print(f"🚫 '{item}' not found in your list.")

        elif choice == '3':
            if shopping_list:
                print("\n📦 Your current shopping list:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("📭 Your shopping list is currently empty.")

        elif choice == '4':
            print("👋 Thanks for using the Shopping List Manager. Happy shopping!")
            break

        else:
            print("❌ Invalid option. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
