monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))
# monthly savings
monthly_savings = monthly_expenses - monthly_income 
# project annual savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(monthly_savings)
print(projected_savings)
