tax_rate = 0.0065

# Getting the lot number of the property.
print("Enter a lot number or 0 to end the program")
lot = float(input("lot number: "))
while lot != 0:
    # Get the value of the property.
    value = float(input("Enter property value: "))

    # calculate the property rate
    p_rate = value * tax_rate

    # Displaying the output
    print(f"Property rate is GH₵{p_rate:,.2f}")

    # Getting the lot number of another property.
    print("Enter a lot number or 0 to end the program")
    lot = float(input("lot number: "))
