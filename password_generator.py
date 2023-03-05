import random
import time
import getpass
from func import valid_answer, valid_number, validator
from string import ascii_uppercase, ascii_lowercase, digits


user_name = str(getpass.getuser())
path = "C:/Users/"+user_name+"/Downloads/Passwords.txt"


digits = digits
lower_letters = ascii_lowercase
upper_letters = ascii_uppercase
symbols = "#!$%&*+-=?@^_"
print("----------Приветствую вас в генераторе паролей----------\n")



def script():
    while True:
        amount = input("Введите количество паролей для генерации: ")
        if valid_number(amount) is True:
            break
        else:
            print("Введите число...")
            continue
    while True:
        long = input("Введите длину одного пароля: ")
        if valid_number(long) is True:
            break
        else:
            print("Введите число...")
            continue
    while True:
        numbers = input("Включать ли цифры (y - Yes, n - No): ")
        if valid_answer(numbers) is True:
            break
        else:
            print("Введите только y или n")
            continue
    while True:
        letters_u = input("Включать ли прописные буквы: ABCDEFGHIJKLMNOPQRSTUVWXYZ (y - Yes, n - No): ")
        if valid_answer(letters_u) is True:
            break
        else:
            print("Введите только y или n")
            continue
    while True:
        letters_l = input("Включать ли строчные буквы: abcdefghijklmnopqrstuvwxyz (y - Yes, n - No): ")
        if valid_answer(letters_l) is True:
            break
        else:
            print("Введите только y или n")
            continue
    while True:
        symbols_1 = input("Включать ли символы: !#$%&*+-=?@^_?: (y - Yes, n - No): ")
        if valid_answer(symbols_1) is True:
            break
        else:
            print("Введите только y или n")
            continue
    while True:
        symbols_2 = input("Исключать ли неоднозначные символы il1Lo0O:O (y - Yes, n - No): ")
        if valid_answer(symbols_2) is True:
            break
        else:
            print("Введите только y или n")
            continue
    print("----------Ваши пароли готовы----------")
    time.sleep(1)
    # file1 = open(path, "w", encoding="utf-8")
    with open(path, "w", encoding="utf-8") as file1:
        for i in range(int(amount)):
            counter = 0
            chars = []
            while counter != int(long):
                if numbers == "y" and counter != int(long):
                    list(digits)
                    chars.append(random.choice(digits))
                    counter += 1
                if letters_l == "y" and counter != int(long):
                    list(lower_letters)
                    chars.append(random.choice(lower_letters))
                    counter += 1
                if letters_u == "y" and counter != int(long):
                    list(upper_letters)
                    chars.append(random.choice(upper_letters))
                    counter += 1
                if symbols_1 == "y" and counter != int(long):
                    list(symbols)
                    chars.append(random.choice(symbols))
                    counter += 1
                if symbols_2 == "y":
                    for j in chars:
                        if j in "il1Lo0O:O":
                            counter2 = chars.count(j)
                            counter -= counter2
                            chars.remove(j)
            random.shuffle(chars)
            print("Пароль:", str("".join(chars)), file=file1)
            print("Пароль: ", *chars, sep="")
    print()
    print(f"Path: {path}")


script()

while True:
    print()
    end_answer = input("Сгенерировать еще паролей: ")
    if valid_answer(end_answer) is True:
        if end_answer == "y":
            time.sleep(1)
            script()
        if end_answer == "n":
            print("See you next time...")
            time.sleep(1)
            # file1.close()
            break
    else:
        print("Введите y или n")
        continue
