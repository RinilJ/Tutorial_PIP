Income=int(input("Enter your income:"))
if Income<250000:
    print("No Income Tax")
elif Income<500000:
    print("Your tax:",Income*0.05)
elif Income<1000000:
    print("Your tax:",Income*0.2)
else:
    print("Your tax:",Income*0.3)
