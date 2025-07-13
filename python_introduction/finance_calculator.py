# prompt user for current monthly income
monthly_income = int(input("enter monthly income"))

# prompt user for total monthy expense
monthly_expense = int(input("enter total monthy expense"))

# Calculate monthy savings
monthly_savings = monthly_income - monthly_expense

# Project annual savings with annual interest rate 5%
Project_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected annual savings after one year, with interest, is: ${Project_annual_savings}.")