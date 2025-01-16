def safe_divide(numerator, denominator):
    # Handing errors like division by zero or non-numeric inputs.
    try:
        # Convert inputs to float
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division
        result = numerator / denominator
        return(f"Result: {result:.1f}")
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    