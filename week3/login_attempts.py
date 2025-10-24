import pandas as db


print("-LOGIN ATTEMPTS- \n")

password_correct = "1234"
max_attempts = 3
attempts = 0
login_success = False

print("--------------------")

while attempts < max_attempts:
  print(f"You're on attempt: {attempts + 1} out of {max_attempts}")
  
  password_try = input("Enter password: \n")
  if password_try == password_correct:
   print("You're in!")
   login_success = True#
   break 

  else:
   attempts += 1
   print(f"Wrong password.")
  
if not login_success:
 print("Congrats, you're locked out of your account now.")
