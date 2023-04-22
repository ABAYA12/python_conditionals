# This program converts speeds in KPH to MPH

KPH = 60             # Assigning the minimum speed in kilometer per hour
MPH = 131            # Assigning the maximum speed in miles per hour
increment = 10       # increment by 10 after the minimum speed in KPH

print("KPH\tMPH")
for kph in range(KPH, MPH, increment):
    mph = kph * 0.6214
    print(f"{kph}\t{mph:.1f}")
