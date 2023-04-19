# Getting user name
name = str(input("What is your name?: "))

# Getting the hours worked and rate per hour
hours = int(input("How many hours did you work this week?: "))

rate = int(input("Enter rate per hour: "))

# Calculating over time
minimumHour = 40
overTime = hours - minimumHour

# Calculating over time wage
overTimeWage = overTime * 1.5 * rate


# Executing conditions

if hours > minimumHour:
    wage = hours * rate
    grossPay = wage + overTimeWage
    print(f"{name}, your pay is ${grossPay:.2f}")

else:
    basicWage = hours * rate
    print(f"{name}, Your pay is ${basicWage:.2f}")
