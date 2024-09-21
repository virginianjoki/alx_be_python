Task = input("enter your task:")
Priority = input("high, medium, low:")
Time_Bound = input("Is it time-bound? (yes/no):")
match priority:
    case "high":
         reminder = (f"{task}is a high priority task ")
    case "medium":
          reminder =(f"{task}is a medium priority task ")   
    case "low":
          reminder = (f"{task} is a low priority task ")
if time_bound == "yes":
     reminder +=  "that requires immediate attention"
else:
     reminder += "Consider completing it when you have free time."     

print(reminder)                 