# Getting user age
age = int(input("Enter your age. It should be number:"))

# Executing conditions

if age <= 1:
    print("You are an infant!")

elif 1 > age < 13:
    print("you are a child!")

elif 13 > age < 20:
    print("You are a teenager!")

else:
    print("You are an adult!")
