

def safe_divide(numerator, denominator):
    try:
        result = float(numerator)/float(denominator)
        return f"The result of the division is {result}"
        
    except ZeroDivisionError:
        return "Cannot divide by zero."
    
    except ValueError:
        return "Please enter numeric values only."
        