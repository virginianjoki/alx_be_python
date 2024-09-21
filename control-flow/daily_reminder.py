task = input("enter your task:")
priority = input("Priority (high/medium/low:)")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        priority_message = "high priority"
        if time_bound == "yes":
            reminder = (f"{task} is a {priority_message} task that requires immediate attention today !")
        else:
            reminder = (f"{task}is a {priority_message} task.Consider completing it when you have free time")
    case "medium":
        priority_message = "medium priority"
        if time_bound =="yes":
            reminder = (f"{task}is a {priority_message} task that requires  attention today !")
        else:
            reminder =  (f"{task}is a {priority_message} task.Consider completing it when you have free time")    
    case "low":
        priority_message = "low priority"
        if time_bound == "yes":
            reminder = (f"{task} is a {priority_message} task. Consider completing it when you have free time today")
        else:
              reminder =  (f"{task}is a {priority_message} task.Consider completing it when you have free time") 

print(f"reminder:{reminder}")              
