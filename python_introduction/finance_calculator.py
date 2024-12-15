# Defining a variable to ask for user monthly income and expenses
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

# Calculating the monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculating project annual savings
annual_interest_rate = 0.05
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * annual_interest_rate)

# Printing result
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")