passwords = [ "Pass123", "SecurePassword1", "weak", "MyP@ssw0rd", "NOLOWER123", "admin", "louvre", "password"]

weak_passwords = ["admin", "louvre", "password", "weak"]

# VALIDATION RULES

# Minimum 8 characters length
# At least one uppercase letter
# At least one lowercase letter
# At least one digit (0-9)


for password in passwords:
    for weak_password in weak_passwords:
        if password == weak_password:
            print(weak_password + " is weak.")
