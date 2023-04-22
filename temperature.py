# Assigning a variable to the maximun temperature
max_temperature = 102.5

# Accepting temperature from the user
temperature = float(input("Eneter the temperature of the vat: "))

# Executimg series of statements
while temperature > max_temperature:
    print('The temperature is too high.')
    print('Turn the thermostat down and wait')
    print('5 minutes. Then take the temperature')
    print('again and enter it.')
    temperature = float(input("Eneter the temperature of the vat: "))

# Reminding the user of the vat full
print('The temperature is acceptable.')
print('Check it again in 15 minutes.')
