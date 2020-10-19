TAX_RATE = .08
STANDARD_DEDUCTION = 30000.0
DEPENDENT_DEDUCTION = 2000.0

gross_income = float(input("What is your gross income? "))
num_dep = int(input("How many dependents do you have? "))

taxable_income = gross_income - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * num_dep
income_tax = taxable_income * TAX_RATE

print("Your income tax is $" + str(round(income_tax, 2)))