# Prompt user for task description and priority
task = input("Enter a task description: ")
priority = input("Enter the task’s priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder = f"Task: {task} is of HIGH priority."
    case "medium":
        reminder = f"Task: {task} is of MEDIUM priority."
    case "low":
        reminder = f"Task: {task} is of LOW priority."
    case _:
        reminder = f"Task: {task} has an UNKNOWN priority."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Provide a customized reminder
print(reminder)
