amt = int(input("Enter the initial amount: "))
rate = float(input("Enter the interest rate (as a decimal): "))
years = int(input("Enter the number of years for investment: "))

print(f"{'Year':<6} {'Final Amount':>12}")
for year in range(1, years + 1):
    f_amt = amt * (1 + rate) ** year
    print(f"{year:<6} {f_amt:12.2f}")
