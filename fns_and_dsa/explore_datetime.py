from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in a readable format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"📅 Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date):
    """Ask the user for a number of days and calculate the future date."""
    try:
        days_to_add = int(input("⏳ Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"🔮 Future date after {days_to_add} day(s): {formatted_future_date}")
    except ValueError:
        print("⚠️ Invalid input. Please enter a valid number of days (integer).")

def main():
    print("🕰️ Welcome to the Date & Time Explorer\n")
    current_date = display_current_datetime()
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()
