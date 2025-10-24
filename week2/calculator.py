# USER CREDENTIALS
user_role = str.casefold(input("What is your role in the company?" + "\n" + "1. Admin" + "\n" + "2. Sales" + "\n" + "3. Marketing" + "\n" + "----------------------" + "\n"))

if user_role == "admin":
    print("Welcome, Admin!")
elif user_role == "sales":
    print("Welcome, Salesperson!")
elif user_role == "marketing":
    print("Welcome, Marketing dude!")
else:
    print("Please try again!")

print("-------------------------")
 
# MAIN MENU
print("This is our company's official tool to calculate your performance thus far.")

print("Choose your desired calculation")
print("1. Profit")
print("2. Margin")
print("3. COMING SOON")

choice = str.casefold(input("Please select what you would like to compute:\n"))

# SIMPLE LOGIC & OPERATIONS

def ask_for_number(amount):
    while True:
        try:
            return float(input(amount))
        except ValueError:
            print("Please enter a valid number.")

def profit():
    print("\n -Let's count your profit-")
    revenue = ask_for_number("Please enter your revenue: \n")
    expenses = ask_for_number("Please enter your expenses: \n")
    profit_count = revenue - expenses
    print(f"-Your profit for this month is {profit_count:.2f}-")
    return profit_count

    # Learner's note : having input syntax inside a function doesnt work, instead
    # define another function for the input part, and refer to the function inside the new one
    # "return" means to exit the current function and take the value thats received.

    # Learner's note 2 : by having f inside the final print, it elevates whats inside,
    # making it possible to get the results of profit_count, instead of printing
    # "profit_count" out, because profit_count is now a VARIABLE PLACEHOLDER

def margin():
    print("\n -Let's count our margins-")
    profit = ask_for_number("Please enter your profit: \n")
    revenue = ask_for_number("Please enter your revenue: \n")
    margin_count = (profit/revenue)*100
    print(f"-Your profit for this month is {margin_count:.2f}%-")
    return margin_count

def coming_soon():
    print("Be patient >:(")

# CHOICES LOGIC & FINAL OUTPUT
    
if choice == "profit":
    print("Result:", profit())

elif choice == "margin":
    print("Result:", margin())

elif choice == "coming soon":
    print("Result:", coming_soon())

else:
    print("No command found")





