Income=int(input("Enter your income:"))
if income<250000:
    print("No Income Tax")
elif income<500000:
    print("Your tax:",Income*0.05)
elif income<1000000:
    print("Your tax:",Income*0.2)
else:
    print("Your tax:",Income*0.3)
