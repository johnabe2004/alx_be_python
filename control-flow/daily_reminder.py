task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
priority = input("Priority (high/medium/low): ").strip().lower()
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
