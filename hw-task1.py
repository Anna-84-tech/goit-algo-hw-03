from datetime import datetime


def get_days_from_today(date: str) -> int:
    """Calculate the number of days between a given date and today.

    Args:
        date (str): A date string in the format 'YYYY-MM-DD' (e.g., '2020-10-09').

    Returns:
        int: The number of days from the given date to today.
             Returns a negative number if the given date is in the future.
             Returns None if the date format is invalid.
    """
    try:
        # Convert the date string to a datetime date object (ignoring hours, minutes, and seconds)
        target_date = datetime.strptime(date, "%Y-%m-%d").date()

        # Get the current date without time
        current_date = datetime.today().date()

        # Calculate the difference and return the number of days as an integer
        difference = current_date - target_date
        return difference.days

    except ValueError:
        # Handle the exception if the input string does not match the 'YYYY-MM-DD' format
        print(f"Error: Invalid date format '{date}'. Please use 'YYYY-MM-DD'.")
        return None


# --- Testing block ---

# 1. Checking a past date (should return a positive number of days)
past_date = "2026-10-09"
print(f"Days between today and {past_date}:", get_days_from_today(past_date))

# 2. Checking a future date (should return a negative number of days)
future_date = "2026-11-01"
print(f"Days between today and {future_date}:", get_days_from_today(future_date))

# 3. Checking error handling with an invalid date format
invalid_date = "10-09-2026"
print(f"Testing error handling for '{invalid_date}':")
get_days_from_today(invalid_date)