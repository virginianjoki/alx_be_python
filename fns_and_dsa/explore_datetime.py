#importing necessary components from the date time module
from datetime import datetime, timedelta

#display the current datetime
def display_current_datetime():
    current_date = datetime.now()

    #format the current date and time   
    formated_date = current_date.strftime("%Y-%m-%d %H:%m:%s")

    print(f" current date and time :{formated_date}")

#calculating future date and time
def calculate_future_date():
    current_date = datetime.now()

    days_to_add = int(input("enter a number of days: "))

    future_date = current_date + timedelta(days = days_to_add)
    
    formated_future_date = future_date.strftime("%Y-%m-%d")

    print(f"future date: {formated_future_date}")

    # Main function to run both parts
def main():
    # Display the current date and time
    display_current_datetime()
   
    # Calculate and display the future date
    calculate_future_date()
 
# Entry point of the script
if __name__ == "__main__":
    main()



    

