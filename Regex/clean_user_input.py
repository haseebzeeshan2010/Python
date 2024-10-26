import re

def clean_phone_number(raw_number):
    remove_char = re.sub(r"\D", "", raw_number)

    if len(remove_char) > 10:
        return None
    
    formatted_number = f"({remove_char[:3]}) {remove_char[3:6]}-{remove_char[6:]}"

    return formatted_number

user_input = input("Enter your phone number: ")

cleaned_number = clean_phone_number(user_input)

if cleaned_number:
    print(cleaned_number)