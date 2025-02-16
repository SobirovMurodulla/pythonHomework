def invest(amount, rate, years):
    new_amount = amount
    for i in range(1,years+1):
        new_amount = new_amount*(1+rate)
        print(f"Year {i}: ${new_amount:.2f}")


amount_input = float(input("Enter initial amount: "))
rate_input = float(input("Enter the rate: "))
years_input = int(input("Enter the number of years: "))
invest(amount_input,rate_input,years_input)


