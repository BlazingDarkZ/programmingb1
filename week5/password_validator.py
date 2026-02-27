import string
import random

def check_min_length(password, min_len=10):
    return len(password) >= min_len


def has_uppercase(password):
    return any(char in string.ascii_uppercase for char in password)


def has_lowercase(password):
    return any(char in string.ascii_lowercase for char in password)


def has_digit(password):
    return any(char in string.digits for char in password)


def has_special_char(password):
    return any(char in string.punctuation for char in password)


def validate_password(password):
    results = {
        "min_length": check_min_length(password),
        "has_uppercase": has_uppercase(password),
        "has_lowercase": has_lowercase(password),
        "has_digit": has_digit(password),
        "has_special": has_special_char(password),
    }

    results["is_valid"] = all(results.values())
    return results


def main():
    print("=" * 40)
    print("This is the Password Validator")
    print("=" * 40)

    print("\nPassword must have:")
    print("- At least 8 characters")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one digit")
    print("- At least one special character")

    password = input("\nEnter your password: ")

    results = validate_password(password)

    print("\nResults:")
    print("Minimum length:", results["min_length"])
    print("Has uppercase:", results["has_uppercase"])
    print("Has lowercase:", results["has_lowercase"])
    print("Has digit:", results["has_digit"])
    print("Has special character:", results["has_special"])

    if results["is_valid"]:
        print("\nPassword is strong")
    else:
        print("\nPassword is weak")


if __name__ == "__main__":
    main()