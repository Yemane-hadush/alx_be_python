from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date
    print(f"Current Date and Time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Update the prompt to match the expected format
    days_to_add = int(input("Enter the number of days to add to the current date: "))  
    current_date = datetime.now()  # Get the current date
    future_date = current_date + timedelta(days=days_to_add)  # Add the specified number of days
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
    print(f"The date after {days_to_add} days will be: {formatted_future_date}")

def main():
    # Call the functions
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
