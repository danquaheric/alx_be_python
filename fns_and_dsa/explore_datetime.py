# explore_datetime.py
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Get the current date and time, save it to `current_date`,
    print it in YYYY-MM-DD HH:MM:SS format and return it.
    """
    current_date = datetime.now()  # required variable name
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(days):
    """
    Calculate the future date by adding `days` to the current date/time.
    Saves the result in `future_date`, prints it in YYYY-MM-DD format and returns it.
    """
    # use the current datetime for calculation (so both date and time are considered)
    current_date = datetime.now()  # keeps consistent naming as requested
    future_date = current_date + timedelta(days=days)  # required variable name
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Part 1: display current date and time
    display_current_datetime()

    # Part 2: prompt user for number of days and calculate future date
    while True:
        user_input = input("Enter the number of days to add to the current date: ").strip()
        try:
            days = int(user_input)
            break
        except ValueError:
            print("Please enter a valid integer for the number of days.")

    calculate_future_date(days)

if __name__ == "__main__":
    main()
