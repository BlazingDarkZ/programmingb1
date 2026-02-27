attempts_list = [("user1","success"),
                 ("user2","success"),
                 ("user3","failed"),
                 ("user1","success"),
                 ("user3","failed"),
                 ("user3","failed")
                 ]

print("CHECKING FOR INCOMPETENT USERS")

# Note 
# Curly brackets are used for dictionaries or set, in this context its a dictionary.
failed_amounts = {}


# Logic to add up the failed amounts
for userid, status in attempts_list:
    if status == "failed":
        if userid in failed_amounts:
            failed_amounts[userid] = failed_amounts[userid] + 1
        else:
            failed_amounts[userid] = 1

# Checking if user has too many wrong attempts

for userid in failed_amounts:
    if failed_amounts[userid] >= 3:
        print("WARNING:" + userid + " has got it wrong " + (str(failed_amounts[userid])) + " times")
