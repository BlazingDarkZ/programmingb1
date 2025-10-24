print("FILTERING EVEN NUMBERS")

set = [1,2,3,4,5,6,7,8,9,10]

print(f"In a set we have the numbers{set}")

for number in set:
    if number %2 != 0:
        continue 
    print(number)

def ask_number():
    number = int(input("enter number"))
    return number

