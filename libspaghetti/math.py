def math(first_number, operator, second_number):
    if operator == "+":
        return int(first_number) + int(second_number)
    elif operator == "-":
        return int(first_number) - int(second_number)
    elif operator == "*":
        return int(first_number) * int(second_number)
    elif operator == "/":
        return int(first_number) / int(second_number)

def math_parser(first_number, first_operator, second_number, second_operator, third_number):
    math_working = []
    if (first_operator in ("/", "*")) and (second_operator in ("+", "-")):
        math_working.insert(0, first_number)
        math_working.insert(1, first_operator)
        math_working.insert(2, second_number)
        if second_operator is not None:
            math_working.insert(3, second_operator)
            math_working.insert(4, third_number)
            math_working.insert(5, "firstFirst")
    elif (second_operator in ("/", "*")) and (first_operator in ("+", "-")):
        math_working.insert(0, first_number)
        math_working.insert(1, first_operator)
        math_working.insert(2, second_number)
        math_working.insert(3, second_operator)
        math_working.insert(4, third_number)
        math_working.insert(5, "secondFirst")
    else:
        math_working.insert(0, first_number)
        math_working.insert(1, first_operator)
        math_working.insert(2, second_number)
        if second_operator is not None:
            math_working.insert(3, second_operator)
            math_working.insert(4, third_number)
            math_working.insert(5, "firstFirst")

    if len(math_working) == 6:
        if math_working[5] == "firstFirst":
            temp = math(math_working[0], math_working[1], math_working[2])
            del math_working[5]
            del math_working[0]
            del math_working[0]
            del math_working[0]
            math_working.insert(0, temp)
            return math(math_working[0], math_working[1], math_working[2])
        elif math_working[5] == "secondFirst":
            temp = math(math_working[2], math_working[3], math_working[4])
            del math_working[5]
            del math_working[4]
            del math_working[3]
            del math_working[2]
            math_working.insert(2, temp)
            return math(math_working[0], math_working[1], math_working[2])
    else:
        return False