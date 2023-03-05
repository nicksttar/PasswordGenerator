def valid_answer(a):
    if a == "y" or a == "n":
        return True
    return False


def valid_number(a):
    if a.isdigit() is True:
        return True
    return False


def validator(question):
    answer = input(question)
    while answer.isdigit() != True:
        answer = input(question)
    return 1
    
class Validator:

    def __init__(self) -> None:
        pass

    def validator(self, question):
        answer = input(question)
        while answer.isdigit() != True:
            answer = input(question)
