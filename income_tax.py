income=float(input('Enter your Annual Income: '))
tax=0
dedu=float(input('Enter deductions (if there\'s Any): '))
ded_income=income-75000-dedu;
if(ded_income<300000):
    print('No Tax to be paid')
elif(ded_income<700000):
    extra=float(ded_income-300000)
    tax=extra*0.05
    print("Tax to be paid = ", tax )
elif(ded_income<1000000):
    extra=float(ded_income-700000)
    tax=20000+extra*0.10
    print("Tax to be paid = ", tax )
elif(ded_income<1200000):
    extra=float(ded_income-1000000)
    tax=50000+extra*0.15
    print("Tax to be paid = ", tax )
elif(ded_income<1500000):
    extra=float(ded_income-1500000)
    tax=80000+extra*0.20
    print("Tax to be paid = ", tax )
elif(ded_income>=1500000):
    extra=float(ded_income-1500000)
    tax=140000+extra*0.30
    print("Tax to be paid = ", tax )
