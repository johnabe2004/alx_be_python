task = input("Enter the task description: ")
priority = input("Enter the task's priority (high/medium/low): ")
time_bound = input("Is the task time-bound? (yes or no): ")
match priority:
        case "high":
            reminder = "Your task '{task}' is of HIGH priority."
        case "medium":
            reminder = "Your task '{task}' is of MEDIUM priority."
        case "low":
            reminder = "Your task '{task}' is of LOW priority."
        case _:
            print("Invalid priority level. Please choose between high, medium, or low.")
       # Check if the task is time-sensitive
if time_bound == "yes":
        reminder += " This is a time-sensitive task that requires immediate attention today!"
        print(reminder)
