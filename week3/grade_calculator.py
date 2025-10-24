print("-WELCOME TO YOUR GRADE CALCULATOR-\n")

grade = int(input("Please input your grade (NO DECIMALS!):\n"))

if grade > 100:
    print("WOW, sadly not possible")
elif grade == 100:
    print("U get a PERFECT SCORE")
elif grade >= 90:
    print("U get a big fat A!")
elif grade >= 80:
    print("U get a B")
elif grade >= 70:
    print("U get a C")
elif grade >= 60:
    print("Good job for passing!")
else:
    print("Im sorry, u failed :(")

