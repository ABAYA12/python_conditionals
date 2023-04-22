# Getting a data to be validated by the while loop.
retail = 'y'

mark_up = 2.5

while retail == "y" or "Y":
    # Get the wholesale cost.
    print("Please provide the wholesale cost")
    wholesale = float(input("wholesale cost: "))

    # Prompting user for enetring wrong value and allowing user to enetr it again
    while wholesale < 0:
        print("Error please, wholesale cost can't be negative or less than 0 ")
        wholesale = float(input("Enter correct wholesale cost: "))

        # Calculating retail price
        retail_price = wholesale * mark_up
        # Display the retail price
        print(f"Your retail price : {retail_price:,.2f}")

    print("Do you want to calculate another retail price?")
    #retail = str(input("enter y or Y for yes: "))
