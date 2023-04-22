salesperson = "y"

# Calculating a series of commision
while salesperson == "y":
    # Taking total sales and commision rate(com_rate)
    sales = float(input("Enter your total sales: "))
    com_rate = float(input("Enter commision rate here: "))

    # Calculating commision
    commision = sales * com_rate

    # Displaying commision
    print(f"Your commision is {commision:,.2f}")
    salesperson = str(
        input("Do you want to calculate another commision? (y/n): "))
