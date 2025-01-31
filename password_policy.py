import re

def check_password_strength(password):
    # Check if password meets minimum requirements
    if len(password) < 8:
        return "Password is too short."
    # Check if has uppercase, lowercase, digits, and special characters
    if not re.search(r"[A-Z]",password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]",password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r"\d",password):
        return "Password must contain at lease one digit."
    if not re.search(r"[!@#$%^&*()]",password):
        return "Password must contain at least one special character."
    return "Password is strong.!"


password = input("Enter a password:")
print(check_password_strength(password))