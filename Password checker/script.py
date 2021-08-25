import re

# at least 8 characters long
# contain any sort of letters, numbers and symbols


pattern = re.compile(
    r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{8,}$")
user_password = input("Please enter your password ")

if re.match(pattern, user_password):
    print("Password match")
else:
    print("Bad password")
