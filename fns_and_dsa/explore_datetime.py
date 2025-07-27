from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    return current_date

def calculate_future_date():
    global future_date
    current_date = datetime.now()
    time_to_add = timedelta(days=future_date)
    new_time = time_to_add + current_date
    new_date = new_time.date()
    return new_date
    

print(f"Current date and time: {display_current_datetime()}")
future_date = int(input("Enter the number of days to add to the current date: "))
print(f"Future date: {calculate_future_date()}")

