# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority using match case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unknown priority level"

# Modify the reminder based on time sensitivity
if time_bound.lower() == "yes":
    reminder += " that requires immediate attention today!"

else:
    if priority in ["high", "medium"]:
        reminder += ". Try to complete it soon."
    else:
        reminder += ". Consider completing it when you have free time."

# Display the customized reminder
print(reminder)
