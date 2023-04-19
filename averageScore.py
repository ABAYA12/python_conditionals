name = str(input("enter your name: "))

# Getting the scores for the three tests
test_1 = int(input("enter your score in test 1: "))
test_2 = int(input("enter your score in test 2: "))
test_3 = int(input("enter your score in test 3: "))
adding_tests = test_1 + test_2 + test_3
averageScore = (adding_tests) / 3

highest_score = 95
if averageScore >= highest_score:
    print("Congratulations", name)
    print("your average is ", averageScore)

else:
    ptint(name, "your average score is", averageScore)
