

pocket_number = int(input("Enter a pocket number: "))

if pocket_number < 0 or pocket_number > 36:
    print("Error: Invalid pocket number")
else:
    if pocket_number == 0:
        print("Pocket is green")

    elif pocket_number >= 1 and pocket_number <= 10:
        if pocket_number % 2 == 0:
            print("Pocket is black")
        else:
            print("Pocket is red")

    elif pocket_number >= 11 and pocket_number <= 18:
        if pocket_number % 2 == 0:
            print("Pocket is red")
        else:
            print("Pocket is black")

    elif pocket_number >= 19 and pocket_number <= 28:
        if pocket_number % 2 == 0:
            print("Pocket is black")
        else:
            print("Pocket is red")

    else:
        if pocket_number % 2 == 0:
            print("Pocket is red")
        else:
            print("Pocket is black")
