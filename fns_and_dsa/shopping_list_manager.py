def display_menu():
    print("\n📋 What would you like to do?")
    print("1. ➕ Add an item to your list")
    print("2. ➖ Remove an item from your list")
    print("3. 👀 View your shopping list")
    print("4. 🚪 Exit the app")

def main():
    shopping_list = []
    print("👋 Hello and welcome to your Shopping List Assistant!")
    print("Let's keep your grocery game strong 💪")

    while True:
        display_menu()
        choice = input("🔢 Please enter your choice (1-4): ").strip()

        if choice == '1':
            item = input("📝 What item would you like to add? ").strip()
            if item:
                shopping_list.append(item)
                print(f"✅ Awesome! '{item}' has been added to your list.")
            else:
                print("⚠️ Hmm, that item name looks empty. Try again.")

        elif choice == '2':
            item = input("❓ Which item would you like to remove? ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"🗑️ Got it! '{item}' has been removed from your list.")
            else:
                print(f"🚫 Uh-oh! '{item}' doesn't seem to be in your list.")

        elif choice == '3':
            if shopping_list:
                print("\n🛍️ Here's what you've got so far:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("📭 Looks like your list is empty. Let's add something!")

        elif choice == '4':
            print("👋 Thanks for using the Shopping List Assistant! Happy shopping! 🛒")
            break

        else:
            print("❌ That wasn’t a valid option. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
