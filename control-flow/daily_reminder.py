# Prompt the user for a task description
task = input("Enter the task description: ")

# Prompt the user for the task's priority (high, medium, low)
priority = input("Enter the task's priority (high, medium, low): ").lower()

# Prompt if the task is time-bound (yes or no)
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Use Match Case for different priority levels
match priority:
    case "high":
        reminder = f"The task '{task}' is of HIGH priority."
    case "medium":
        reminder = f"The task '{task}' is of MEDIUM priority."
    case "low":
        reminder = f"The task '{task}' is of LOW priority."
    case _:
        reminder = "Invalid priority level entered."

# Check if the task is time-bound
if time_bound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"
else:
    reminder += " This task is not time-sensitive."

# Print the customized reminder
print(reminder)
