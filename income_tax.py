annual_income = float(input('Enter your Annual Income: '))
total_tax = 0
deductions = float(input('Enter deductions (if there\'s any): '))
taxable_income = annual_income - 75000 - deductions

if taxable_income < 300000:
    print('No Tax to be paid')
elif taxable_income < 700000:
    additional_income = taxable_income - 300000
    total_tax = additional_income * 0.05
    print("Tax to be paid =", total_tax)
elif taxable_income < 1000000:
    additional_income = taxable_income - 700000
    total_tax = 20000 + additional_income * 0.10
    print("Tax to be paid =", total_tax)
elif taxable_income < 1200000:
    additional_income = taxable_income - 1000000
    total_tax = 50000 + additional_income * 0.15
    print("Tax to be paid =", total_tax)
elif taxable_income < 1500000:
    additional_income = taxable_income - 1200000
    total_tax = 80000 + additional_income * 0.20
    print("Tax to be paid =", total_tax)
elif taxable_income >= 1500000:
    additional_income = taxable_income - 1500000
    total_tax = 140000 + additional_income * 0.30
    print("Tax to be paid =", total_tax)
