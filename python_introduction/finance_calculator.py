# Prompt the user for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, are: ${projected_savings:.2f}.")
