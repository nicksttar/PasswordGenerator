import random
import time
import getpass
from functions import validator, password_results


user_name = str(getpass.getuser())
path = "C:/Users/"+user_name+"/Downloads/Passwords.txt"


print("----------Wellcome to password generator----------\n")


def script():

    amount = validator("Enter the number of passwords to generate: ")
    long = validator("Enter the length of one password: ")
    numbers = validator("Whether to include numbers: ", categoty="string")
    letters_u = validator("Whether to include uppercase letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ: ", categoty="string")
    letters_l = validator("Whether to include lowercase letters: abcdefghijklmnopqrstuvwxyz: ", categoty="string")
    symbols_1 = validator("Whether to include symbols: #!$%&*+-=?@^_: ", categoty="string")
    symbols_2 = validator("Whether to exclude ambiguous characters il1Lo0O:O: ", categoty="string")

    print("----------Your passwords are ready----------")
    time.sleep(1)
    results = password_results(amount, long, numbers, letters_u, letters_l, symbols_1, symbols_2)
    with open(path, "a", encoding="utf-8") as file_output:
        for password in results:
            print(f"Пароль: {password}")
            print(f"Пароль: {password}", file=file_output)

    print(f"{path}\n")

    end_answer = validator("Generate more passwords?: ", categoty="string")
    if end_answer == "y":
        time.sleep(1)
        script()
    elif end_answer == "n":
        print("See you next time")
        time.sleep(1)


script()
