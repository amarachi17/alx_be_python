# Defining a variable to ask for user monthly income and expenses
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

# Calculating the monthly savings
monthly_savings = monthly_expenses - monthly_income

# Calculating project annual savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Printing result
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")