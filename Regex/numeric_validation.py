import re

def numeric_validation(input_pattern):
    pattern = r"^\d+$"
    match = re.search(pattern, input_pattern)
    return match is not None

user_input = input("Enter a number")

if numeric_validation(user_input):
    print("Valid")
else:
    print("Invalid")