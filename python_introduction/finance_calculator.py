#finance_calculator
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly Expenses: "))
monthly_saving = monthly_income - monthly_expenses
projected_saving = float(monthly_saving * 12 + (monthly_saving * 12 * 0.05))
print("Your projected saving is:", projected_saving)
