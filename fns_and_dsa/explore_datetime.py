from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date

def calculate_future_date():
    global days_to_add
    current_date = datetime.now()
    time_to_add = timedelta(days=days_to_add)
    future_date = time_to_add + current_date
    future_date_fr = future_date.strftime("%Y-%m-%d")
    return future_date_fr
    

print(f"Current date and time: {display_current_datetime()}")
days_to_add = int(input("Enter the number of days to add to the current date: "))
print(f"Future date: {calculate_future_date()}")

