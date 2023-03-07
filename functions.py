from random import sample
from string import ascii_uppercase, ascii_lowercase, digits

digits = digits
lower_letters = ascii_lowercase
upper_letters = ascii_uppercase
symbols = "#!$%&*+-=?@^_"

def validator(question, categoty="digit", params=("y", "n")):
    """Anty-dump validator"""
    if categoty == "digit":
        user_input = input(question)
        while user_input.isdigit() != True:
            user_input = input(f"Write {categoty}: ")
        return int(user_input)
    elif categoty == "string":
        user_input = input(question)
        while user_input.lower() not in params:
            user_input = input(f"Write {params}: ")
        return user_input.lower()
    
def password_results(amount, long, numbers="n", letters_u="n", letters_l="n", symbols_1="n", symbols_2="n"):
    all_passwords = []
    for i in range(amount):
        one_password = ""
        if numbers == "y":
            one_password += digits
        if letters_u == "y":
            one_password += upper_letters
        if letters_l == "y":
            one_password += lower_letters
        if symbols_1 == "y":
            one_password += symbols
        elif symbols_2 == "y":
            for i in "il1Lo0O:O":
                if i in one_password:
                    one_password = one_password.replace(i, "")
        all_passwords.append("".join(sample(list(one_password), long)))
    return all_passwords
