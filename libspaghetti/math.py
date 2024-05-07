def math(first_number, operator, second_number):
    if operator == "+":
        return int(first_number) + int(second_number)
    elif operator == "-":
        return int(first_number) - int(second_number)
    elif operator == "*":
        return int(first_number) * int(second_number)
    elif operator == "/":
        return int(first_number) / int(second_number)


def math_parser(first_number=None, first_operator=None, second_number=None, second_operator=None, third_number=None, which_first=None):
    if (first_number != None) and (first_operator == None):
        temp = str(first_number).split(" ")
        first_number = temp[0]
        first_operator = temp[1]
        second_number = temp[2]
        if len(temp) > 3:
            second_operator = temp[3]
            third_number = temp[4]
    math_working = []
    if which_first == "l":
        math_working.insert(0, first_number)
        math_working.insert(1, first_operator)
        math_working.insert(2, second_number)
        if second_operator is not None:
            math_working.insert(3, second_operator)
            math_working.insert(4, third_number)
            math_working.insert(5, "firstFirst")
    elif which_first == "r":
        math_working.insert(0, first_number)
        math_working.insert(1, first_operator)
        math_working.insert(2, second_number)
        math_working.insert(3, second_operator)
        math_working.insert(4, third_number)
        math_working.insert(5, "secondFirst")
    else:
        if (first_operator in ("/", "*")):
            math_working.insert(0, first_number)
            math_working.insert(1, first_operator)
            math_working.insert(2, second_number)
            if (second_operator != None) and (second_operator in ("+", "-")):
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
        return math(math_working[0], math_working[1], math_working[2])

# print(math_parser("1 + 3"))