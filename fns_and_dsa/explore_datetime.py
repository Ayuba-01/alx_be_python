import datetime


def display_current_datetime():
    current_date = datetime.datetime.now()
    return current_date

def calculate_future_date():
    global future_date
    current_date = datetime.datetime.now()
    time_to_add = datetime.timedelta(days=future_date)
    new_time = time_to_add + current_date
    return new_time
    

print(f"Current date and time: {display_current_datetime()}")
future_date = int(input("Enter the number of days to add to the current date: "))
print(f"Future date: {calculate_future_date()}")

