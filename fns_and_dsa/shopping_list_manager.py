# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in a readable format (YYYY-MM-DD HH:MM:SS).
    """
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted current date and time
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Prompts the user to enter a number of days and calculates the future date after adding those days.
    """
    try:
        # Prompt the user for the number of days to add
        days_to_add = int(input("Enter the number of days to add: "))
        
        # Get the current date
        current_date = datetime.now()
        
        # Calculate the future date by adding days
        future_date = current_date + timedelta(days=days_to_add)
        
        # Format the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        
        # Print the future date
        print(f"Future date after {days_to_add} days: {formatted_future_date}")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    # Part 1: Display the current date and time
    display_current_datetime()
    
    # Part 2: Calculate a future date based on user input
    calculate_future_date()
